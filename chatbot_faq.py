import tkinter as tk
from tkinter import ttk

# 1. Clean, Curated FAQ Database (Mapped 1-to-1 for 100% accurate responses)
FAQ_MENU = {
    "📦 Where is my order / tracking?": 
        "Bro, tracking it won't make it arrive faster. It's giving 'impatient'. Let the courier cook, your package is vibing in transit somewhere.",
    
    "💰 Can I get a refund or return?": 
        "Refund? In this economy? It’s giving broke behavior. Check the receipt bestie, all sales are final. No take-backsies.",
    
    "💸 Why are your prices so high?": 
        "High prices? Sounds like a skill issue. Use code 'BROKE20' for 20% off if you're down bad, but quality isn't cheap, bestie.",
    
    "💎 Is this product actually legit?": 
        "Main character energy only. Our products are certified bussin', no cap. If you think it's fake, you're trippin'.",
    
    "👤 Let me speak to a human agent.": 
        "A human? Be real, humans are mid. You are talking to the final boss of AI support. Select a question or cry about it.",
    
    "👋 Just saying hi / sup!": 
        "Sup fam! Welcome to the loop. Ask me something smart or prepare to get roasted. What's the move?",
    
    "🛠️ Who built this bot?": 
        "I was coded by Florence, an AI Engineering Intern at CodeAlpha. They gave me this massive brain to roast you with."
}

# Custom Rich-Text Insertion to guarantee Emojis render on Windows
def insert_rich_text(text_widget, text, base_tag):
    for char in text:
        if ord(char) > 0xFFFF or ord(char) in [9792, 9794, 9874, 9875, 9993, 10024]: 
            text_widget.insert(tk.END, char, (base_tag, "emoji"))
        else:
            text_widget.insert(tk.END, char, base_tag)

# Click Handler for Questions
def ask_question(question_text):
    if question_text in FAQ_MENU:
        chat.config(state='normal')
        
        # Print User's Selected Question (Clean, Right-aligned)
        insert_rich_text(chat, "You\n", "user_header")
        insert_rich_text(chat, f"{question_text}\n\n", "user_text")
        
        # Print Bot's Response (Left-aligned)
        bot_reply = FAQ_MENU[question_text]
        insert_rich_text(chat, "Sassy Bot\n", "bot_header")
        insert_rich_text(chat, f"{bot_reply}\n\n\n", "bot_text")
        
        chat.config(state='disabled')
        chat.yview(tk.END)

# Button Hover Animations
def on_enter(e, btn):
    btn.config(bg="#ff79c6", fg="#12121a")

def on_leave(e, btn):
    btn.config(bg="#1e1f2f", fg="#ff79c6")

# --- UI Setup ---
root = tk.Tk()
root.title("Gen-Z Support Lounge v5.0")
root.geometry("950x650")  # Widescreen layout
root.configure(bg="#0c0d14")
root.resizable(True, True)

# Top Status Bar
top_bar = tk.Frame(root, bg="#131421", height=70)
top_bar.pack(fill=tk.X, side=tk.TOP)
top_bar.pack_propagate(False)

status_title = tk.Label(top_bar, text="💅 GEN-Z AI LOUNGE", font=("Segoe UI", 14, "bold"), fg="#ff79c6", bg="#131421")
status_title.pack(anchor="w", padx=(25, 0), pady=(12, 0))

status_sub = tk.Label(top_bar, text="● Interactive Dashboard • 100% Match Accuracy", font=("Segoe UI", 9), fg="#00f0ff", bg="#131421")
status_sub.pack(anchor="w", padx=(25, 0))

# Main Workspace (Split Pane)
workspace = tk.Frame(root, bg="#0c0d14")
workspace.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# --- LEFT PANE: Chat Log ---
chat_frame = tk.Frame(workspace, bg="#0c0d14")
chat_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

chat = tk.Text(chat_frame, bg="#12121e", fg="#f8f8f2", font=("Segoe UI", 11), wrap="word", 
               state='disabled', bd=0, highlightthickness=1, highlightbackground="#282a36", 
               spacing1=4, spacing3=4, padx=15, pady=15)
chat.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Formatting tags
chat.tag_config("user_header", justify="right", foreground="#00f0ff", font=("Segoe UI Semibold", 9))
chat.tag_config("user_text", justify="right", foreground="#f8f8f2", font=("Segoe UI", 11))
chat.tag_config("bot_header", justify="left", foreground="#bd93f9", font=("Segoe UI Semibold", 9))
chat.tag_config("bot_text", justify="left", foreground="#ffffff", font=("Segoe UI", 11))
chat.tag_config("emoji", font=("Segoe UI Emoji", 11))

scrollbar = ttk.Scrollbar(chat_frame, orient="vertical", command=chat.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat.configure(yscrollcommand=scrollbar.set)

# --- RIGHT PANE: Interactive Menu ---
menu_frame = tk.Frame(workspace, bg="#131421", bd=0, highlightthickness=1, highlightbackground="#282a36", width=380)
menu_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
menu_frame.pack_propagate(False)

menu_title = tk.Label(menu_frame, text="SELECT A QUESTION TO ASK:", font=("Segoe UI", 10, "bold"), fg="#6272a4", bg="#131421")
menu_title.pack(anchor="w", padx=20, pady=(20, 15))

# Create stylized, clickable Question Cards
for question in FAQ_MENU.keys():
    btn = tk.Button(
        menu_frame, 
        text=question, 
        anchor="w",
        font=("Segoe UI Semibold", 10), 
        bg="#1e1f2f", 
        fg="#ff79c6", 
        activebackground="#ff79c6", 
        activeforeground="#12121a", 
        bd=0, 
        cursor="hand2", 
        padx=15, 
        pady=12,
        command=lambda q=question: ask_question(q)
    )
    btn.pack(fill=tk.X, padx=20, pady=6)
    
    # Bind premium hover states
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

# Setup initial welcoming message
chat.config(state='normal')
insert_rich_text(chat, "Sassy Bot\n", "bot_header")
insert_rich_text(chat, "Sup! Welcome to my lounge. Don't waste my time typing garbage. Just click any of the questions on the right and prepare to be judged. What's the move? 💅\n\n\n", "bot_text")
chat.config(state='disabled')

root.mainloop()
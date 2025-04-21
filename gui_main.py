import tkinter as tk
import subprocess
from tkinter import messagebox
import pygame

# --- Initialize Pygame Mixer for Sound ---
pygame.mixer.init()

def play_click_sound():
    try:
        pygame.mixer.Sound("click.wav").play()
    except Exception as e:
        print(f"Sound error: {e}")

# --- Button Functions ---
def open_encode():
    play_click_sound()
    subprocess.Popen(["python", "gui_encode.py"])

def open_decode():
    play_click_sound()
    subprocess.Popen(["python", "gui_decode.py"])

def exit_app():
    play_click_sound()
    window.destroy()

def show_about():
    play_click_sound()
    messagebox.showinfo(
        "About SteganoGraphy",
        "🔐 SteganoGraphy App\n\nThis app lets you hide secret messages inside images (encoding),\n"
        "and extract hidden messages from images (decoding).\n\nDeveloped by Renuka 💻✨"
    )

# --- GUI Setup ---
window = tk.Tk()
window.title("SteganoGraphy Main Menu")
window.geometry("400x350")
window.configure(bg="#e0f7fa")

# --- Title Label ---
tk.Label(window, text="Welcome to SteganoGraphy", font=("Segoe UI", 16, "bold"),
         bg="#e0f7fa", fg="#00796B").pack(pady=30)

# --- Buttons ---
tk.Button(window, text="🔐 Encode Message", font=("Segoe UI", 12), width=25,
          bg="#4CAF50", fg="white", command=open_encode).pack(pady=10)

tk.Button(window, text="🔓 Decode Message", font=("Segoe UI", 12), width=25,
          bg="#2196F3", fg="white", command=open_decode).pack(pady=10)

tk.Button(window, text="❓ About / Help", font=("Segoe UI", 12), width=25,
          bg="#FFC107", fg="black", command=show_about).pack(pady=10)

tk.Button(window, text="❌ Exit", font=("Segoe UI", 12), width=25,
          bg="#f44336", fg="white", command=exit_app).pack(pady=10)

# --- Menu Bar ---
menu_bar = tk.Menu(window)
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)
window.config(menu=menu_bar)

# --- Run App ---
window.mainloop()

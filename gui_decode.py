import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog
from PIL import Image

# --- Function to Decode from a Single Image ---
def decode_message(image_path, entered_password):
    try:
        img = Image.open(image_path)
        width, height = img.size
        decoded_chars = []

        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                decoded_chars.append(chr(r))
                if "".join(decoded_chars).endswith("$t3g0"):
                    full_message = "".join(decoded_chars[:-5])  # remove marker
                    if ":" in full_message:
                        password, secret = full_message.split(":", 1)
                        if password == entered_password:
                            return secret
                        else:
                            return "❌ Incorrect password"
                    else:
                        return "⚠️ Message found but no password detected."
        return None  # No marker found
    except Exception as e:
        return f"❌ Error with {image_path}: {str(e)}"

# --- Browse Multiple Images ---
def browse_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_paths:
        image_paths_var.set(file_paths)
        decode_button.config(state=tk.NORMAL)

# --- Decode All Selected Images ---
def decode_all():
    files = image_paths_var.get()
    if not files:
        messagebox.showwarning("No Images", "Please select image(s) to decode.")
        return

    # Ask password before decoding
    entered_password = simpledialog.askstring("🔐 Enter Password", "Please enter the decoding password:", show='*')
    if not entered_password:
        messagebox.showinfo("Cancelled", "Decoding cancelled. No password entered.")
        return

    results_text.delete(1.0, tk.END)

    for img_path in files:
        message = decode_message(img_path, entered_password)
        if message:
            if message == "❌ Incorrect password" or message.startswith("⚠️"):
                results_text.insert(tk.END, f"{message} in '{img_path.split('/')[-1]}'\n\n")
            else:
                results_text.insert(tk.END, f"✅ Message from '{img_path.split('/')[-1]}':\n{message}\n\n")
        else:
            results_text.insert(tk.END, f"ℹ️ No hidden message found in '{img_path.split('/')[-1]}'\n\n")

# --- GUI Setup ---
window = tk.Tk()
window.title("🔓 SteganoGraphy - Decode Messages")
window.geometry("600x500")
window.configure(bg="#f9f9f9")

tk.Label(window, text="🔍 Select Images to Scan for Hidden Messages", font=("Segoe UI", 13, "bold"), bg="#f9f9f9").pack(pady=20)

tk.Button(window, text="📁 Browse Images", font=("Segoe UI", 11), bg="#4CAF50", fg="white", command=browse_images).pack(pady=10)

decode_button = tk.Button(window, text="🔓 Decode Messages", font=("Segoe UI", 11, "bold"), bg="#2196F3", fg="white", command=decode_all, state=tk.DISABLED)
decode_button.pack(pady=10)

results_text = scrolledtext.ScrolledText(window, width=70, height=20, font=("Segoe UI", 10))
results_text.pack(padx=20, pady=20)

image_paths_var = tk.Variable()

window.mainloop()

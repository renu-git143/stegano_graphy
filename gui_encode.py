import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# --- Encode Message into Image ---
def encode_message_into_image(img_path, message, password):
    try:
        img = Image.open(img_path)
        encoded = img.copy()
        width, height = img.size

        full_message = f"{password}:{message}$t3g0"
        binary_data = [ord(c) for c in full_message]

        if len(binary_data) > width * height:
            return "❌ Message too long for selected image."

        data_index = 0
        for row in range(height):
            for col in range(width):
                if data_index < len(binary_data):
                    r, g, b = img.getpixel((col, row))
                    encoded.putpixel((col, row), (binary_data[data_index], g, b))
                    data_index += 1
                else:
                    break

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if save_path:
            encoded.save(save_path)
            return f"✅ Message encoded and saved to:\n{save_path}"
        else:
            return "❌ Save cancelled."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# --- Browse Image ---
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        image_path_var.set(file_path)

# --- Encode Action ---
def encode_action():
    img_path = image_path_var.get()
    message = message_entry.get("1.0", tk.END).strip()
    password = password_entry.get().strip()

    if not img_path or not message or not password:
        messagebox.showwarning("Missing Data", "Please select image, enter message and password.")
        return

    result = encode_message_into_image(img_path, message, password)
    messagebox.showinfo("Encoding Result", result)

# --- GUI Setup ---
window = tk.Tk()
window.title("🔒 SteganoGraphy - Encode Message with Password")
window.geometry("600x500")
window.configure(bg="#f0f8ff")

tk.Label(window, text="📁 Select Image to Hide Message", font=("Segoe UI", 13, "bold"), bg="#f0f8ff").pack(pady=20)
tk.Button(window, text="Browse Image", font=("Segoe UI", 11), bg="#4CAF50", fg="white", command=browse_image).pack()

image_path_var = tk.StringVar()
tk.Label(window, textvariable=image_path_var, font=("Segoe UI", 10), bg="#f0f8ff", wraplength=550).pack(pady=10)

tk.Label(window, text="💬 Enter Secret Message:", font=("Segoe UI", 11), bg="#f0f8ff").pack(pady=5)
message_entry = tk.Text(window, height=5, width=60, font=("Segoe UI", 10))
message_entry.pack(pady=5)

tk.Label(window, text="🔑 Enter Password:", font=("Segoe UI", 11), bg="#f0f8ff").pack(pady=5)
password_entry = tk.Entry(window, show='*', font=("Segoe UI", 10), width=40)
password_entry.pack(pady=5)

tk.Button(window, text="🔐 Encode & Save", font=("Segoe UI", 11, "bold"), bg="#2196F3", fg="white", command=encode_action).pack(pady=20)

window.mainloop()

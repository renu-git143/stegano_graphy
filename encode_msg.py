# encode_msg.py

from PIL import Image

def encode_message(image_path, message, output_path):
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    encoded_img = img.copy()
    message += "$t3g0"
    msg_index = 0

    for row in range(height):
        for col in range(width):
            if msg_index >= len(message):
                encoded_img.save(output_path)
                print("✅ Message encoded and saved as:", output_path)
                return
            r, g, b = img.getpixel((col, row))
            ascii_val = ord(message[msg_index])
            encoded_img.putpixel((col, row), (ascii_val, g, b))
            msg_index += 1

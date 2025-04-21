def decode_message(image_path):
    try:
        img = Image.open(image_path).convert("RGB")  # Convert to RGB to avoid alpha issues
        width, height = img.size
        decoded_chars = []

        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                    continue  # Skip if not standard RGB pixel
                decoded_chars.append(chr(r))
                if "".join(decoded_chars).endswith("$t3g0"):
                    return "".join(decoded_chars[:-5])  # Exclude the marker

        return None  # No marker found
    except Exception as e:
        return f"❌ Error with {image_path}: {str(e)}"

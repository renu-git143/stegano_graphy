from PIL import Image #python imaging library used for easy read, modify and save image 

def encode_message(image_path, message, output_path): #here we are taking variables for input, hidden msg, and output
    img = Image.open(image_path) #image_path reads all the images in the folder so that it will be easy to read any image 
    img = img.convert("RGB")  # Ensure RGB mode for lsb interaction
    width, height = img.size #to count no of pixels so that we can know how far ecoding loop is consodered 

    message += "$t3g0"  # end marker Think of "$t3g0" like a full stop at the end of a sentence —It tells the decoder
    encoded_img = img.copy() #Creates a copy of the original image, where we’ll make the changes

    msg_index = 0
    for row in range(height): #for every row check pixels 
        for col in range(width):
            if msg_index >= len(message): #if end marker is found thn the loop stops 
                encoded_img.save(output_path)
                print("✅ Message encoded and saved as:", output_path)
                return

            r, g, b = img.getpixel((col, row))
            ascii_val = ord(message[msg_index])
            encoded_img.putpixel((col, row), (ascii_val, g, b))
            msg_index += 1

# Example usage
encode_message("sample.png", "Hello, world! 💌", "encoded_image.png")
#later we can do this into dynamic interaction
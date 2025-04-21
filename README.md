# SteganoGraphy

**SteganoGraphy** is a Python-based desktop application that allows users to hide and extract secret text messages within image files using steganography techniques. The project provides a GUI interface to make the process simple and user-friendly.

##  Features

- **Text Encoding**: Hide text inside images.
- **Text Decoding**: Retrieve hidden messages from images.
- **User Interface**: GUI built using `Tkinter`.
- **Multiple Sample Images** included.
- Organized module structure for easy understanding.

## 🖼 GUI Files

- `gui_main.py` – Main GUI launcher
- `gui_encode.py` – Encode interface
- `gui_decode.py` – Decode interface
- `welcome_screen.py` – Intro screen

##  Logic Files

- `encode_msg.py` – Encoding logic
- `decode_msg.py` – Decoding logic
- `extra.py` – Additional utilities

## Sample Images

- `sample.png`, `maybe.png`, `like12.png`, `guess.png`, etc.
- `encoded_image.png` – Example of output with hidden message

## Tech Stack

- Python
- Tkinter
- PIL (Pillow)

## How to Install

1. Clone the Repository open a terminal or command prompt and run
   
   git clone : 
   https://github.com/renu-git143/SteganoGraphy123.git
   
   cd SteganoGraphy123

2. Install Required Dependencies 

   pip install -r requirements.txt

3. Run the main screen 

   python welcome_screen.py

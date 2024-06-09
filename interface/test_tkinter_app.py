import os
import sys
import subprocess
from pathlib import Path
import sqlite3
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

script_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir, "assets", "frame6")

def relative_to_assets(path: str) -> str:
    full_path = os.path.join(ASSETS_PATH, path)
    print(f"Checking path: {full_path}")  # Debug print statement
    if not os.path.exists(full_path):
        print(f"File does not exist: {full_path}")  # Debug print statement
    return full_path

# Placeholder function to avoid NameError
def mover_pessoa1_para_antigos():
    print("mover_pessoa1_para_antigos called")

# Placeholder function to avoid NameError
def pesquisar():
    print("pesquisar called")

# Example usage in your setup
window = Tk()
window.geometry("950x680")
window.configure(bg="#FFFFFF")
window.title("Sistema de Condomínio")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=680,
    width=950,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Load images
try:
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    print("entry_1.png loaded successfully")
except Exception as e:
    print(f"Failed to load entry_1.png: {e}")

try:
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    print("entry_2.png loaded successfully")
except Exception as e:
    print(f"Failed to load entry_2.png: {e}")

try:
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    print("entry_3.png loaded successfully")
except Exception as e:
    print(f"Failed to load entry_3.png: {e}")

try:
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    print("button_1.png loaded successfully")
except Exception as e:
    print(f"Failed to load button_1.png: {e}")

try:
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    print("button_2.png loaded successfully")
except Exception as e:
    print(f"Failed to load button_2.png: {e}")

# Create entries and buttons
entry_bg_1 = canvas.create_image(205, 83, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#F5F5F5", highlightthickness=0)
entry_1.place(x=66, y=70, width=278, height=26)

entry_bg_2 = canvas.create_image(482, 83, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#F5F5F5", highlightthickness=0)
entry_2.place(x=389, y=70, width=186, height=26)

entry_bg_3 = canvas.create_image(667, 83, image=entry_image_3)
entry_3 = Entry(bd=0, bg="#F5F5F5", highlightthickness=0)
entry_3.place(x=617, y=70, width=100, height=26)

button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=mover_pessoa1_para_antigos, relief="flat")
button_1.place(x=30, y=240, width=414, height=54)

button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=pesquisar, relief="flat")
button_2.place(x=752, y=61, width=214, height=51)

# Keep references to the images to prevent garbage collection
global_images = [button_image_1, button_image_2, button_image_3]

window.mainloop()
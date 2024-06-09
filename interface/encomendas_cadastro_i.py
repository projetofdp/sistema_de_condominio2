import sys
import sqlite3
import re
import subprocess
import os
import back
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


script_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir, "assets", "frame9")


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)

def voltar():
    args = [sys.executable, str(OUTPUT_PATH / "dashboard_i.py")]
    subprocess.run(args)

def pesquisar():
    nome = entry_1.get()
    bloco = entry_2.get()
    apartamento = entry_3.get()
    
    if nome and bloco and apartamento:  # Verifica se todos os campos estão preenchidos
        abrir_edicao([nome, bloco, apartamento])
        window.destroy()
    else:
        messagebox.showinfo("Erro", "Por favor, preencha todos os campos.")

def cadastrar():
    nome = entry_5.get()
    bloco = entry_6.get()
    apartamento = entry_8.get()
    data_entrega = entry_7.get()
    porteiro = entry_4.get()
    back.inserir_encomenda(nome, data_entrega, bloco, apartamento, porteiro)

def abrir_edicao(dados):
    if len(dados) == 3:
        args = [sys.executable, str(OUTPUT_PATH / "cadastro_pesquisa_I.py")] + list(map(str, dados))
        subprocess.run(args)
    else:
        messagebox.showerror("Erro", "Dados insuficientes para abrir a edição.")

window = Tk()

window.geometry("950x680")
window.configure(bg = "#FFFFFF")
window.title("Sistema de Condomínio")


canvas = Canvas( window, bg = "#FFFFFF", height = 680, width = 950, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)

#textos do frame
canvas.create_text( 555.0, 86.0, anchor="nw", text="Pesquisa", fill="#8EBC4F", font=("BeVietnamPro Bold", 45 * -1))
canvas.create_text(784.0, 22.0, anchor="nw", text="encomendas", fill="#B9B9B9", font=("BeVietnamPro Light", 19 * -1))
canvas.create_text( 69.0, 86.0, anchor="nw", text="Cadastro", fill="#8EBC4F", font=("BeVietnamPro Bold", 45 * -1))

button_image_2 = PhotoImage( file=relative_to_assets("button_2.png"))
button_2 = Button( image=button_image_2, borderwidth=0, highlightthickness=0, command=voltar, relief="flat")
button_2.place( x=36.0, y=34.0, width=30.0, height=15.0)

#entrada nome pesquisa
canvas.create_text( 555.0, 164.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_1 = PhotoImage( file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(711.0,201.66262912750244,image=entry_image_1)
entry_1 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place( x=564.0, y=186.0, width=294.0, height=29.325258255004883)

#entrada bloco pesquisa
canvas.create_text( 555.0, 223.0, anchor="nw", text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_2 = PhotoImage( file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image( 625.0, 260.66262912750244, image=entry_image_2)
entry_2 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place( x=564.0, y=245.0, width=122.0, height=29.325258255004883)

#entrada apartamento pesquisa
canvas.create_text( 727.0, 223.0, anchor="nw", text="apartamento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_3 = PhotoImage( file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image( 797.0, 260.66262912750244, image=entry_image_3)
entry_3 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_3.place( x=736.0, y=245.0, width=122.0, height=29.325258255004883)

button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
button_1 = Button( image=button_image_1, borderwidth=0, highlightthickness=0, command=pesquisar, relief="flat")
button_1.place( x=655.0, y=299.0, width=112.0, height=40.78125)

#cadastro

#nome cadastro
canvas.create_text( 75.0, 161.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_5 = PhotoImage( file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image( 231.0, 198.66262912750244, image=entry_image_5)
entry_5 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_5.place( x=84.0, y=183.0, width=294.0, height=29.325258255004883)

#bloco cadastro
canvas.create_text( 75.0, 221.0, anchor="nw", text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_6 = PhotoImage( file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image( 152.5, 258.66262912750244, image=entry_image_6)
entry_6 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_6.place( x=84.0, y=243.0, width=137.0, height=29.325258255004883)

#apartamento cadastro
canvas.create_text( 250.0, 221.0, anchor="nw", text="apartamento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_8 = PhotoImage( file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image( 327.5, 258.66262912750244, image=entry_image_8)
entry_8 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_8.place( x=259.0, y=243.0, width=137.0, height=29.325258255004883)

# data cadastro
canvas.create_text( 75.0, 281.0, anchor="nw", text="data:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_7 = PhotoImage( file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image( 152.5, 318.66262912750244, image=entry_image_7)
entry_7 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_7.place( x=84.0, y=303.0, width=137.0, height=29.325258255004883)

 #entrada porteiro
canvas.create_text( 76.0, 338.0, anchor="nw", text="porteiro:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_4 = PhotoImage( file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image( 153.5, 375.66262912750244, image=entry_image_4)
entry_4 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_4.place( x=85.0, y=360.0, width=137.0, height=29.325258255004883)

#cadastro button
button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
button_3 = Button( image=button_image_3, borderwidth=0, highlightthickness=0, command=cadastrar, relief="flat")
button_3.place( x=67.0, y=401.0, width=115.0, height=40.78125)


window.resizable(False, False)
window.mainloop()

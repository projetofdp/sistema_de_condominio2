import sys
import sqlite3
import re
import subprocess
import os
import back
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


# Adicionando o caminho do script de banco de dados
script_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir, "assets", "frame4")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)

def pesquisar():
    nome = entry_2.get()
    bloco = entry_7.get()
    apartamento = entry_8.get()
    
    if nome and bloco and apartamento:  # Verifica se todos os campos estão preenchidos
        abrir_edicao([nome, bloco, apartamento])
        window.destroy()
    else:
        messagebox.showinfo("Erro", "Por favor, preencha todos os campos.")

def abrir_edicao(dados):
    if len(dados) == 3:
        args = [sys.executable, str(OUTPUT_PATH / "cadastro_moradores_editar_i.py")] + list(map(str, dados))
        subprocess.run(args)
    else:
        messagebox.showerror("Erro", "Dados insuficientes para abrir a edição.")

def cadastrar():
    nome = entry_1.get()
    cpf = entry_3.get()
    data_nascimento = entry_10.get()
    telefone = entry_9.get()
    bloco = entry_4.get()
    apartamento = entry_6.get()
    placa_carro = entry_5.get()
    back.inserir_morador(nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro)

def voltar():
    args = [sys.executable, str(OUTPUT_PATH / "dashboard_i.py")]
    subprocess.run(args)

# Configuração da janela principal
window = Tk()
window.geometry("950x680")
window.configure(bg = "#FFFFFF")
window.title("Sistema de Condomínio")

canvas = Canvas( window, bg = "#FFFFFF", height = 680, width = 950, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_rectangle( 473.0, 84.0, 475.0, 584.0, fill="#FFFFFF", outline="")

# Botões e entradas
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button( image=button_image_1, borderwidth=0, highlightthickness=0, command= cadastrar, relief="flat")
button_1.place(x=67.0, y=527.0, width=112.0, height=40.78125)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button( image=button_image_2, borderwidth=0, highlightthickness=0, command= pesquisar, relief="flat")
button_2.place(x=640.0, y=293.0, width=114.0, height=40.78125)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button( image=button_image_3, borderwidth=0, highlightthickness=0, command= voltar, relief="flat")
button_3.place(x=39.0, y=35.0, width=30.0, height=15.0)

canvas.create_text( 694.0, 26.0, anchor="nw", text="cadastro de moradores", fill="#B9B9B9", font=("BeVietnamPro Light", 19 * -1))

canvas.create_text( 69.0, 80.0, anchor="nw", text="Cadastro", fill="#8EBC4F", font=("BeVietnamPro Bold", 45 * -1))

canvas.create_text( 540.0, 80.0, anchor="nw", text="Pesquisa", fill="#8EBC4F", font=("BeVietnamPro Bold", 45 * -1))

canvas.create_text( 73.0, 158.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image( 229.0, 195.66262912750244, image=entry_image_1)
entry_1 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place( x=82.0, y=180.0, width=294.0, height=29.325258255004883)

canvas.create_text( 540.0, 158.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
# entrada nome pesquisa
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(696.0, 195.66262912750244, image=entry_image_2)
entry_2 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place( x=549.0, y=180.0, width=294.0, height=29.325258255004883)

canvas.create_text( 73.0, 217.0, anchor="nw", text="cpf:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image( 181.0, 254.66262912750244, image=entry_image_3)
entry_3 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_3.place( x=82.0, y=239.0, width=198.0, height=29.325258255004883)

canvas.create_text( 71.0, 394.0, anchor="nw", text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image( 148.5, 431.66262912750244, image=entry_image_4)
entry_4 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_4.place( x=80.0, y=416.0, width=137.0, height=29.325258255004883)

canvas.create_text( 71.0, 453.0, anchor="nw", text="placa do carro:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image( 148.5, 490.66262912750244, image=entry_image_5)
entry_5 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_5.place( x=80.0, y=475.0, width=137.0, height=29.325258255004883)

canvas.create_text( 246.0, 394.0, anchor="nw", text="apartamento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image( 323.5, 431.66262912750244, image=entry_image_6)
entry_6 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_6.place( x=255.0, y=416.0, width=137.0, height=29.325258255004883)

canvas.create_text( 540.0, 217.0, anchor="nw", text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))

# entrada bloco pesquisa
entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(610.0, 254.66262912750244, image=entry_image_7)
entry_7 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_7.place( x=549.0, y=239.0, width=122.0, height=29.325258255004883)

canvas.create_text(712.0,217.0,anchor="nw",text="apartamento:",fill="#000000",font=("BeVietnamPro SemiBold", 17 * -1))

# entrada apartamento pesquisa
entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image( 782.0, 254.66262912750244, image=entry_image_8)
entry_8 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_8.place(x=721.0, y=239.0, width=122.0, height=29.325258255004883)

canvas.create_text( 73.0, 335.0, anchor="nw", text="telefone:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))

entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image( 181.0, 372.66262912750244, image=entry_image_9)
entry_9 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_9.place( x=82.0, y=357.0, width=198.0, height=29.325258255004883)

canvas.create_text( 71.0, 276.0, anchor="nw", text="data de nascimento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))

entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image( 179.0, 313.66262912750244, image=entry_image_10)
entry_10 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_10.place( x=80.0, y=298.0, width=198.0, height=29.325258255004883)

window.resizable(False, False)
window.mainloop()

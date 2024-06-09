import os
import sqlite3
import subprocess
import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


script_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir, "assets", "frame2")


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


def voltar():
    args = [sys.executable, str(OUTPUT_PATH / "encomendas_cadastro_i.py")]
    subprocess.run(args)

def novas():
    args = [sys.executable, str(OUTPUT_PATH / "encomendas_pesquisa_i.py")]
    subprocess.run(args)

def obter_informacoes_encomendas():
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nome, apartamento, bloco, data_entrega, data_retirada, porteiro, nome_de_quem_retirou
        FROM encomenda
        ORDER BY data_entrega ASC, data_retirada ASC
    """)
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def atualizar_dados_canvas(canvas,resultados):
    # Limpa apenas os elementos dinâmicos do canvas
    for item in canvas.find_withtag("dinamico"):
        canvas.delete(item)

    for i, dado in enumerate(resultados[:3]):  # Limita a três resultados
        nome, data_entrega, data_retirada, bloco, apartamento, Id, porteiro,nome_de_quem_retirou = dado
        if i == 0:
            preencher_pessoa1(nome, data_entrega, data_retirada, bloco, apartamento, Id, porteiro,nome_de_quem_retirou)
        elif i == 1:
            preencher_pessoa2(nome, data_entrega, data_retirada, bloco, apartamento, Id, porteiro,nome_de_quem_retirou)
        elif i == 2:
            preencher_pessoa3(nome, data_entrega, data_retirada, bloco, apartamento, Id, porteiro,nome_de_quem_retirou)

def preencher_pessoa1(nome, data_entrega, data_retirada, bloco, apartamento, Id, porteiro,nome_de_quem_retirou):
    canvas.create_text( 72.0, 137.0, anchor="nw", text=nome, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text( 274.0, 177.0, anchor="nw", text=data_entrega, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 274.0, 224.0, anchor="nw", text=data_retirada, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 162.0, 228.0, anchor="nw", text=bloco, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 450.0, 219.0, anchor="nw", text=apartamento, fill="#545454", font=("BeVietnamPro Medium", 12 * -1), tags="dinamico")
    canvas.create_text( 72.0, 182.0, anchor="nw", text=nome_de_quem_retirou, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text( 114.0, 228.0, anchor="nw", text=Id, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 276.0, 137.0, anchor="nw", text=porteiro, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

def preencher_pessoa2(nome, data_entrega, data_retirada, bloco, apartamento, Id, porteiro,nome_de_quem_retirou):
    canvas.create_text( 72.0, 296.0, anchor="nw", text=nome, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text( 274.0, 336.0, anchor="nw", text=data_entrega, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 274.0, 383.0, anchor="nw", text=data_retirada, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 72.0, 341.0, anchor="nw", text= nome_de_quem_retirou, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text( 276.0, 296.0, anchor="nw", text=porteiro, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 450.0, 378.0, anchor="nw", text=Id, fill="#545454", font=("BeVietnamPro Medium", 12 * -1), tags="dinamico")
    canvas.create_text( 114.0, 387.0, anchor="nw", text=apartamento, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 162.0, 387.0, anchor="nw", text=bloco, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

def preencher_pessoa3(nome, data_entrega, data_retirada, bloco, apartamento, Id, porteiro,nome_de_quem_retirou):
    canvas.create_text( 72.0, 455.0, anchor="nw", text=nome, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text( 274.0, 495.0, anchor="nw", text=data_entrega, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 274.0, 542.0, anchor="nw", text=data_retirada, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 72.0, 500.0, anchor="nw", text=nome_de_quem_retirou, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text( 276.0, 455.0, anchor="nw", text=porteiro, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 450.0, 537.0, anchor="nw", text= Id, fill="#545454", font=("BeVietnamPro Medium", 12 * -1), tags="dinamico")
    canvas.create_text( 114.0, 546.0, anchor="nw", text=apartamento, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 162.0, 546.0, anchor="nw", text=bloco, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")


window = Tk()

window.geometry("950x680")
window.configure(bg = "#FFFFFF")
window.title("Sistema de Condomínio")


canvas = Canvas( window, bg = "#FFFFFF", height = 680, width = 950, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text( 790.0, 23.0, anchor="nw", text="encomendas", fill="#B9B9B9", font=("BeVietnamPro Light", 19 * -1))
button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
button_3 = Button( image=button_image_3, borderwidth=0, highlightthickness=0, command=voltar, relief="flat")
button_3.place( x=42.0, y=35.0, width=30.0, height=15.0)


canvas.create_text( 72.0, 127.0, anchor="nw", text="nome", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 72.0, 217.0, anchor="nw", text="Unidade Vinculada", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 274.0, 166.0, anchor="nw", text="data da entrega", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 274.0, 213.0, anchor="nw", text="data da retirada", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 72.0,171.0,anchor="nw", text="quem retirou", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 276.0, 127.0, anchor="nw", text="porteiro", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 72.0, 228.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1))
canvas.create_text( 126.0, 228.0, anchor="nw", text="apto", fill="#000000", font=("BeVietnamPro Medium", 14 * -1))



button_image_2 = PhotoImage( file=relative_to_assets("button_2.png"))
button_2 = Button( image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
button_2.place( x=440.0, y=134.0, width=70.0, height=18.214290618896484)




image_image_1 = PhotoImage( file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image( 292.0, 189.0, image=image_image_1)


canvas.create_text( 72.0, 286.0, anchor="nw", text="nome", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 72.0, 376.0, anchor="nw", text="Unidade Vinculada", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 274.0, 325.0, anchor="nw", text="data da entrega", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 274.0, 372.0, anchor="nw", text="data da retirada", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 72.0, 330.0, anchor="nw", text="quem retirou", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 276.0, 286.0, anchor="nw", text="porteiro", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 72.0, 387.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1))
canvas.create_text( 126.0, 387.0, anchor="nw", text="apto", fill="#000000", font=("BeVietnamPro Medium", 14 * -1))

button_image_4 = PhotoImage( file=relative_to_assets("button_4.png"))
button_4 = Button( image=button_image_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_4 clicked"), relief="flat")
button_4.place( x=440.0, y=293.0, width=70.0, height=18.214290618896484)

image_image_2 = PhotoImage( file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image( 292.0, 348.0, image=image_image_2)


canvas.create_text( 72.0, 445.0, anchor="nw", text="nome", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 72.0, 535.0, anchor="nw", text="Unidade Vinculada", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 274.0, 484.0, anchor="nw", text="data da entrega", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 274.0, 531.0, anchor="nw", text="data da retirada", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 72.0, 489.0, anchor="nw", text="quem retirou", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 276.0, 445.0, anchor="nw", text="porteiro", fill="#545454", font=("BeVietnamPro Medium", 11 * -1))
canvas.create_text( 72.0, 546.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1))
canvas.create_text( 126.0, 546.0, anchor="nw", text="apto", fill="#000000", font=("BeVietnamPro Medium", 14 * -1))


button_image_5 = PhotoImage( file=relative_to_assets("button_5.png"))
button_5 = Button( image=button_image_5, borderwidth=0, highlightthickness=0, command=lambda: print("button_5 clicked"), relief="flat")
button_5.place( x=440.0, y=452.0, width=70.0, height=18.214290618896484)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image( 292.0, 507.0, image=image_image_3)


button_image_6 = PhotoImage( file=relative_to_assets("button_6.png"))
button_6 = Button( image=button_image_6, borderwidth=0, highlightthickness=0, command=lambda: print("button_6 clicked"), relief="flat")
button_6.place( x=242.0, y=67.0, width=180.0, height=40.0)

button_image_7 = PhotoImage( file=relative_to_assets("button_7.png"))
button_7 = Button( image=button_image_7, borderwidth=0, highlightthickness=0, command=novas, relief="flat")
button_7.place( x=62.0, y=67.0, width=180.0, height=40.0)

resultados = obter_informacoes_encomendas()
atualizar_dados_canvas(canvas, resultados)

window.resizable(False, False)
window.mainloop()

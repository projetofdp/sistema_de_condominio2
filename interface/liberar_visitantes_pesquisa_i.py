import os
import sys
import subprocess
from pathlib import Path
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

script_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir, "assets", "frame7")

def abrir_arquivo_python_com_resultados(resultados):
    nome_morador, bloco, apartamento = resultados

def buscar_visitantes(nome_morador, bloco, apartamento):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    query = """
        SELECT v.nome_visitante, v.horario1, v.horario2, v.data, v.bloco, v.apartamento, m.nome
        FROM visitantes v
        INNER JOIN moradores m ON v.morador_id = m.id
        WHERE 1=1
    """
    params = []
    if nome_morador:
        query += " AND m.nome LIKE ?"
        params.append(f"%{nome_morador}%")
    if bloco:
        query += " AND v.bloco = ?"
        params.append(bloco)
    if apartamento:
        query += " AND v.apartamento = ?"
        params.append(apartamento)

    cursor.execute(query, params)
    resultados_visitantes = cursor.fetchall()

    conn.close()
    return (resultados_visitantes)

def atualizar_dados_canvas(resultados):
    # Limpa apenas os elementos dinâmicos do canvas
    for item in canvas.find_withtag("dinamico"):
        canvas.delete(item)

    for i, dado in enumerate(resultados):
        nome = dado[0]
        hora1 = dado[1]
        hora2 = dado[2]
        data = dado[3]
        bloco = dado[4]
        apto = dado[5]
        if i == 0:
            preencher_pessoa1(nome, hora1, hora2, data, bloco, apto)
        elif i == 1:
            preencher_pessoa2(nome, hora1, hora2, data, bloco, apto)
        elif i == 2:
            preencher_pessoa3(nome, hora1, hora2, data, bloco, apto)

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)

def preencher_pessoa1(nome, data, hora1, hora2, bloco, apto):
    criar_elemetos_pessoa1()
    canvas.create_text( 87.0, 305.0, anchor="nw", text=nome, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text( 242.0, 309.0, anchor="nw", text=data, fill="#000000", font=("BeVietnamPro Medium", 14 * -1),tags="dinamico")
    canvas.create_text( 87.0, 349.0, anchor="nw", text=hora1, fill="#000000", font=("BeVietnamPro Medium", 14 * -1),tags="dinamico")
    canvas.create_text(153.0,349.0,anchor="nw",text=hora2, fill="#000000",font=("BeVietnamPro Medium", 14 * -1) ,tags="dinamico")
    canvas.create_text(284.0,349.0,anchor="nw",text=bloco,fill="#000000",font=("BeVietnamPro Medium", 14 * -1) ,tags="dinamico")
    canvas.create_text( 332.0, 349.0, anchor="nw", text=apto, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

def preencher_pessoa2(nome, data, hora1, hora2, bloco, apto):
    criar_elemetos_pessoa2()
    canvas.create_text( 87.0, 458.0, anchor="nw", text=nome, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text( 242.0, 462.0, anchor="nw", text=data, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 87.0, 502.0, anchor="nw", text=hora1, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 153.0, 502.0, anchor="nw", text=hora2, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 284.0, 502.0, anchor="nw", text=bloco,fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 332.0, 502.0, anchor="nw", text=apto, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

def preencher_pessoa3(nome, data, hora1, hora2, bloco, apto):
    criar_elemetos_pessoa3()
    canvas.create_text( 87.0, 152.0, anchor="nw",text=nome, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 242.0, 156.0, anchor="nw", text=data, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 87.0, 196.0, anchor="nw", text=hora1, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 153.0, 196.0, anchor="nw", text=hora2, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 284.0, 196.0, anchor="nw", text=bloco, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 332.0, 196.0, anchor="nw", text=apto, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

def voltar():
    args = [sys.executable, str(OUTPUT_PATH / "liberar_visitantes_i.py")]
    subprocess.run(args)


window = Tk()

window.geometry("950x680")
window.configure(bg = "#FFFFFF")
window.title("Sistema de Condomínio")


canvas = Canvas(window,bg = "#FFFFFF",height = 680,width = 950,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=voltar,relief="flat")
button_1.place( x=69.0, y=34.0, width=30.0, height=15.0)
canvas.create_text( 724.0, 25.0, anchor="nw", text="Liberar visitantes", fill="#B9B9B9", font=("BeVietnamPro Light", 19 * -1))

def criar_elemetos_pessoa1():
    global image_image_1
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image( 221.0, 349.0, image=image_image_1 , tags="dinamico")
    canvas.create_text( 87.0, 337.0, anchor="nw", text="horário", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 337.0, anchor="nw", text="Unidade Vinculada", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 87.0, 296.0, anchor="nw", text="nome", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 241.0, 297.0, anchor="nw", text="data", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 349.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(296.0,349.0,anchor="nw",text="apto",fill="#000000",font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(136.0, 349.0, anchor="nw", text="ás", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")


button_image_2 = PhotoImage( file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=lambda: print("button_2 clicked"),relief="flat")
button_2.place( x=184.0, y=380.0, width=69.0, height=21.327281951904297)

def criar_elemetos_pessoa2():
    global image_image_2
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(221.0,502.0,image=image_image_2)
    canvas.create_text( 87.0, 490.0, anchor="nw", text="horário", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 490.0, anchor="nw", text="Unidade Vinculada", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 87.0, 449.0, anchor="nw", text="nome", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 241.0, 450.0, anchor="nw", text="data", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 502.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 296.0, 502.0, anchor="nw", text="apto", fill="#000000",font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 136.0, 502.0, anchor="nw", text="ás", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")


button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0,highlightthickness=0,command=lambda: print("button_3 clicked"),relief="flat")
button_3.place( x=184.0, y=533.0, width=69.0, height=21.327281951904297)
def criar_elemetos_pessoa3():
    global image_image_3
    image_image_3 = PhotoImage( file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(221.0,196.0,image=image_image_3 , tags="dinamico")
    canvas.create_text(87.0, 184.0, anchor="nw", text="horário", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 184.0,anchor="nw", text="Unidade Vinculada", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 87.0, 143.0, anchor="nw", text="nome", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 241.0, 144.0, anchor="nw", text="data", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 196.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 296.0, 196.0, anchor="nw", text="apto", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 136.0, 196.0,  anchor="nw", text="ás", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")


button_image_4 = PhotoImage( file=relative_to_assets("button_4.png"))
button_4 = Button( image=button_image_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_4 clicked"), relief="flat")
button_4.place( x=184.0, y=227.0, width=69.0, height=21.327281951904297)

button_image_6 = PhotoImage( file=relative_to_assets("button_6.png"))
button_6 = Button( image=button_image_6, borderwidth=0, highlightthickness=0, command=lambda: print("button_6 clicked"), relief="flat")

button_6.place( x=73.0, y=77.0, width=180.0, height=40.0)
window.resizable(False, False)
window.mainloop()

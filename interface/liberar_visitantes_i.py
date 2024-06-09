import os
import sys
import subprocess
from pathlib import Path
import sqlite3
from tkinter import Tk, Canvas, Frame, Entry, Text, Button, PhotoImage

script_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir,"assets" ,"frame6")


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)

def obter_informacoes_do_banco_de_dados():
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.nome_visitante, v.horario1, v.horario2, v.data, v.bloco, v.apartamento, m.nome
        FROM visitantes v
        INNER JOIN moradores m ON v.morador_id = m.id
        ORDER BY v.data ASC, v.horario1 ASC, v.horario2 ASC
    """)
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def mover_pessoa1_para_antigos():
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()

    # Seleciona os dados da primeira pessoa e do morador relacionado
    cursor.execute("""
        SELECT v.id, v.nome_visitante, v.horario1, v.horario2, v.data, v.bloco, v.apartamento, m.id, m.nome
        FROM visitantes v
        INNER JOIN moradores m ON v.morador_id = m.id
        ORDER BY v.data ASC, v.horario1 ASC, v.horario2 ASC
        LIMIT 1
    """)
    pessoa = cursor.fetchone()

    if pessoa:
        visitante_id, nome_visitante, horario1, horario2, data, bloco, apartamento, morador_id, nome_morador = pessoa

        # Move os dados para a tabela visitantes_antigos
        cursor.execute("""
            INSERT INTO visitantes_antigos (morador_id, nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (morador_id, nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento))

        # Remove os dados da primeira pessoa da tabela visitantes
        cursor.execute("""
            DELETE FROM visitantes 
            WHERE id = ?
        """, (visitante_id,))

        conn.commit()

    conn.close()

    # Atualiza o canvas com os novos dados
    resultados = obter_informacoes_do_banco_de_dados()
    atualizar_dados_canvas(resultados)

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

def preencher_pessoa1(nome, hora1, hora2, data, bloco, apto):
    canvas.create_text(115, 173, anchor="nw", text=nome, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text(115, 213, anchor="nw", text=hora1, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(181, 213, anchor="nw", text=hora2, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(270, 173, anchor="nw", text=data, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(310, 213, anchor="nw", text=bloco, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(355, 213, anchor="nw", text=apto, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

def preencher_pessoa2(nome, hora1, hora2, data, bloco, apto):
    canvas.create_text(115, 326, anchor="nw", text=nome, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text(115, 366, anchor="nw", text=hora1, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(181, 366, anchor="nw", text=hora2, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(270, 326, anchor="nw", text=data, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(310, 366, anchor="nw", text=bloco, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(355, 366, anchor="nw", text=apto, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

def preencher_pessoa3(nome, hora1, hora2, data, bloco, apto):
    canvas.create_text(115, 479, anchor="nw", text=nome, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text(115, 519, anchor="nw", text=hora1, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(181, 519, anchor="nw", text=hora2, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(270, 479, anchor="nw", text=data, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(310, 519, anchor="nw", text=bloco, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(355, 519, anchor="nw", text=apto, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")


def pesquisar():
    global resultados
    nome_morador = entry_1.get()
    bloco = entry_2.get()
    apartamento = entry_3.get()
    resultados = (nome_morador, bloco, apartamento)
    abrir_arquivo_python_com_resultados(resultados)

def abrir_arquivo_python_com_resultados(resultados):
    args = [sys.executable, str(OUTPUT_PATH / "liberar_visitantes_pesquisa_i.py")] + list(map(str, resultados))
    subprocess.run(args)

def voltar():
    args = [sys.executable, str(OUTPUT_PATH / "dashboard_i.py")]
    subprocess.run(args)

# Criar a janela principal
window = Tk()

window.geometry("950x680")
window.configure(bg="#FFFFFF")
window.title("Sistema de Condomínio")

# Criar o canvas
canvas = Canvas( window, bg="#FFFFFF", height=680, width=950, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

buttons_dinamicos = []


image_image_3 = PhotoImage( file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image( 249.0, 213.0, image=image_image_3, tags="dinamico")
canvas.create_text( 115.0, 201.0, anchor="nw", text="horário", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text(  270.0, 201.0, anchor="nw", text="Unidade Vinculada", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text( 115.0, 161.0, anchor="nw", text="nome", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text(269.0, 161.0, anchor="nw", text="data", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text( 270.0, 213.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
canvas.create_text(324.0, 213.0, anchor="nw", text="apto", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
canvas.create_text(160.0, 213.0, anchor="nw", text="ás", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")


button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
button_3 = Button( image=button_image_3, borderwidth=0, highlightthickness=0, command=mover_pessoa1_para_antigos, relief="flat")
button_3.place( x=212, y=244, width=69, height=21.327281951904297)
buttons_dinamicos.append(button_3)




image_image_1 = PhotoImage( file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(249.0,366.0, image=image_image_1 , tags="dinamico")
canvas.create_text( 115.0, 354.0, anchor="nw", text="horário", fill="#8C8C8C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text( 270.0, 354.0, anchor="nw", text="Unidade Vinculada", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text( 115.0, 314.0, anchor="nw", text="nome", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text( 269.0, 314.0, anchor="nw", text="data", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text(  270.0,  366.0,  anchor="nw",  text="bloco ",  fill="#000000",  font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
canvas.create_text( 324.0, 366.0, anchor="nw", text="apto", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
canvas.create_text( 160.0, 366.0, anchor="nw", text="ás", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
button_1 = Button( image=button_image_1, borderwidth=0, highlightthickness=0, command=mover_pessoa1_para_antigos, relief="flat")
button_1.place( x=212.0, y=397.0, width=69.0, height=21.327281951904297)
buttons_dinamicos.append(button_1)



image_image_2 = PhotoImage( file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image( 249.0, 519.0, image=image_image_2 , tags="dinamico")
canvas.create_text( 115.0, 507.0, anchor="nw", text="horário", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text( 270.0, 507.0, anchor="nw", text="Unidade Vinculada", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text( 115.0, 467.0, anchor="nw", text="nome", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text( 269.0, 467.0,  anchor="nw",  text="data",  fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
canvas.create_text( 270.0, 519.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
canvas.create_text( 324.0, 519.0, anchor="nw", text="apto", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
canvas.create_text( 160.0, 519.0, anchor="nw", text="ás", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

button_image_2 = PhotoImage( file=relative_to_assets("button_2.png"))
button_2 = Button( image=button_image_2, borderwidth=0, highlightthickness=0, command=mover_pessoa1_para_antigos, relief="flat")
button_2.place( x=212.0, y=550.0, width=69.0, height=21.327281951904297)
buttons_dinamicos.append(button_2)

# textos diversos
canvas.create_text(45.0, 66.0, anchor="nw", text="hoje", fill="#8EBC4F",font=("BeVietnamPro SemiBold", 45 * -1))
canvas.create_text( 539.0, 66.0, anchor="nw", text="Pesquisa", fill="#8EBC4F", font=("BeVietnamPro Bold", 45 * -1))
canvas.create_text(724.0, 25.0, anchor="nw", text="Liberar visitantes", fill="#B9B9B9",font=("BeVietnamPro Light", 19 * -1))


#pesquisa
canvas.create_text(539.0,144.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
canvas.create_text(539.0,203.0,anchor="nw",text="bloco:",fill="#000000",font=("BeVietnamPro SemiBold", 17 * -1))
canvas.create_text(711.0,203.0,anchor="nw",text="apartamento:",fill="#000000",font=("BeVietnamPro SemiBold", 17 * -1))

#botão pesquisar
button_image_4 = PhotoImage( file=relative_to_assets("button_4.png"))
button_4 = Button( image=button_image_4, borderwidth=0, highlightthickness=0, command=pesquisar, relief="flat")
button_4.place( x=639.0, y=279.0, width=115.0, height=40.78125)

#entrada nome
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(695.0,181.66262912750244,image=entry_image_1)
entry_1 = Entry( bd=0, bg="#FFFFFF", fg="#000716",highlightthickness=0)
entry_1.place( x=548.0, y=166.0,width=294.0,height=29.325258255004883)

#entrada bloco
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(609.0, 240.66262912750244,image=entry_image_2)
entry_2 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
entry_2.place(x=548.0,y=225.0, width=122.0, height=29.325258255004883)

#entrada apto
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(781.0,240.66262912750244,image=entry_image_3)
entry_3 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
entry_3.place(x=720.0,y=225.0,width=122.0,height=29.325258255004883)

#botão voltar
button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=voltar,relief="flat")
button_5.place( x=69.0,y=34.0,width=30.0,height=15.0)
canvas.create_rectangle(474.0, 90.0, 476.0, 590.0, fill="#FFFFFF", outline="")



resultados = obter_informacoes_do_banco_de_dados()
atualizar_dados_canvas(resultados)


window.resizable(False, False)
window.mainloop()
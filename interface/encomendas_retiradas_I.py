import subprocess
import sys
import os
import json
from pathlib import Path
from funcoesdb import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

script_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir, "assets", "frame1")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)

def voltar():
    args = [sys.executable, str(OUTPUT_PATH / "encomendas_pesquisa_i.py")]
    subprocess.run(args)

if len(sys.argv) > 1:
        encomenda_data_json = sys.argv[1]
        encomenda_data = json.loads(encomenda_data_json)

if len(sys.argv) > 1:
    encomenda_data_json = sys.argv[1]
    encomenda_data = json.loads(encomenda_data_json)
    
    nome = encomenda_data["nome"]
    bloco = encomenda_data["bloco"]
    apartamento = encomenda_data["apartamento"]
    porteiro = encomenda_data["porteiro"]
    data_entrega = encomenda_data["data_entrega"]
    id_ = encomenda_data["id"]



def preencher_entrega():
    entry_nome_entrega.config(state="normal")
    entry_bloco_entrega.config(state="normal")
    entry_apartamento_entrega.config(state="normal")
    entry_data_entrega.config(state="normal")
    entry_porteiro_entrega.config(state="normal")

    entry_nome_entrega.insert(0,nome)
    entry_bloco_entrega.insert(0, bloco)
    entry_apartamento_entrega.insert(0, apartamento)
    entry_data_entrega.insert(0, data_entrega)
    entry_porteiro_entrega.insert(0, porteiro)
    
    entry_nome_entrega.config(state="readonly")
    entry_bloco_entrega.config(state="readonly")
    entry_apartamento_entrega.config(state="readonly")
    entry_data_entrega.config(state="readonly")
    entry_porteiro_entrega.config(state="readonly")

def retirada():
    nome_de_quem_retirou = entry_nome_de_quem_retirou.get()
    cpf = entry_cpf_retirada.get()
    bloco_retirada = entry_bloco_retirada.get()
    porteiro = entry_porteiro.get()
    apartamento_retirada = entry_apartamento_retirada.get()
    data_retirada = entry_data_retirada.get()

     # Verificar se o bloco e o apartamento correspondem aos dados de entrega
    bloco_entrega = entry_bloco_entrega.get()
    apartamento_entrega = entry_apartamento_entrega.get()

    if bloco_retirada == bloco_entrega and apartamento_retirada == apartamento_entrega:
        # Se correspondem, chama a função para atualizar as informações no banco de dados
        inserir_informacoes_encomendas_antigas(nome, apartamento, bloco, data_entrega, data_retirada, porteiro, cpf, nome_de_quem_retirou)

        apagar_dados_outra_tabela(id_)

        limpar_entradas()
    else:
        # Caso contrário, exibe uma mensagem de erro
        messagebox.showerror("Erro", "Você não é morador e não pode retirar a encomenda.")

def limpar_entradas():
    # Limpar as entradas de retirada
    entry_nome_de_quem_retirou.delete(0, 'end')
    entry_cpf_retirada.delete(0, 'end')
    entry_bloco_retirada.delete(0, 'end')
    entry_apartamento_retirada.delete(0, 'end')
    entry_data_retirada.delete(0, 'end')

    # Limpar as entradas de entrega
    entry_nome_entrega.delete(0, 'end')
    entry_bloco_entrega.delete(0, 'end')
    entry_apartamento_entrega.delete(0, 'end')
    entry_data_entrega.delete(0, 'end')
    entry_porteiro_entrega.delete(0, 'end')


window = Tk()

window.geometry("950x680")
window.configure(bg = "#FFFFFF")
window.title("Sistema de Condomínio")

canvas = Canvas( window, bg = "#FFFFFF", height = 680, width = 950, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)
canvas.create_text( 559.0, 70.0, anchor="nw", text="retirada", fill="#8EBC4F", font=("BeVietnamPro SemiBold", 45 * -1))
canvas.create_text( 64.0, 70.0, anchor="nw", text="entrega", fill="#8EBC4F", font=("BeVietnamPro SemiBold", 45 * -1))
canvas.create_text( 782.0, 21.0, anchor="nw", text="encomendas", fill="#B9B9B9", font=("BeVietnamPro Light", 19 * -1))

button_image_2 = PhotoImage( file=relative_to_assets("button_2.png"))
button_2 = Button( image=button_image_2, borderwidth=0, highlightthickness=0, command=voltar, relief="flat")
button_2.place( x=34.0, y=33.0, width=30.0, height=15.0)


#entrada nome retirada
canvas.create_text( 562.0, 133.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_nome_de_quem_retirou = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_nome_de_quem_retirou = canvas.create_image( 718.0, 170.66262912750244, image=entry_image_nome_de_quem_retirou)
entry_nome_de_quem_retirou = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_nome_de_quem_retirou.place( x=571.0, y=155.0, width=294.0, height=29.325258255004883)

#entrada cpf retirada
canvas.create_text( 562.0,192.0,anchor="nw", text="cpf:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_retirada = PhotoImage( file=relative_to_assets("entry_2.png"))
entry_bg_retirada = canvas.create_image( 670.0, 229.66262912750244, image=entry_image_retirada)
entry_cpf_retirada = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_cpf_retirada.place( x=571.0, y=214.0, width=198.0, height=29.325258255004883)

#entrada bloco retirada
canvas.create_text(562.0, 251.0, anchor="nw" ,text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_bloco_retirada = PhotoImage( file=relative_to_assets("entry_3.png"))
entry_bg_bloco_retirada = canvas.create_image( 639.5, 288.66262912750244, image=entry_image_bloco_retirada)
entry_bloco_retirada = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_bloco_retirada.place( x=571.0, y=273.0, width=137.0, height=29.325258255004883)

#entrada porteiro retirada
canvas.create_text( 562.0, 310.0, anchor="nw", text="porteiro:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_porteiro = PhotoImage( file=relative_to_assets("entry_4.png"))
entry_bg_porteiro = canvas.create_image( 645.0, 347.66262912750244, image=entry_image_porteiro)
entry_porteiro = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_porteiro.place( x=571.0, y=332.0, width=148.0, height=29.325258255004883)

#entrada apartamento retirada
canvas.create_text(737.0, 251.0, anchor="nw", text="apartamento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_apartamento_retirada = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_apartamento_retirada = canvas.create_image(814.5, 288.66262912750244, image=entry_image_apartamento_retirada)
entry_apartamento_retirada = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_apartamento_retirada.place(x=746.0, y=273.0, width=137.0, height=29.325258255004883)

#entrada data retirada
canvas.create_text( 562.0, 370.0, anchor="nw", text="data:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_data_retirada = PhotoImage( file=relative_to_assets("entry_6.png"))
entry_bg_data_retirada = canvas.create_image( 645.0, 407.66262912750244, image=entry_image_data_retirada)
entry_data_retirada = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_data_retirada.place( x=571.0, y=392.0, width=148.0, height=29.325258255004883)


#entrada nome entrega
canvas.create_text( 64.0, 133.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_nome_entrega = PhotoImage( file=relative_to_assets("entry_11.png"))
entry_bg_nome_entrega = canvas.create_image( 220.0, 170.66262912750244, image=entry_image_nome_entrega)
entry_nome_entrega= Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_nome_entrega.place(  x=73.0, y=155.0, width=294.0, height=29.325258255004883)

#entrada bloco entrega
canvas.create_text( 64.0, 193.0, anchor="nw", text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_bloco_entrega = PhotoImage( file=relative_to_assets("entry_9.png"))
entry_bg_bloco_entrega = canvas.create_image( 141.5, 230.66262912750244, image=entry_image_bloco_entrega)
entry_bloco_entrega = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_bloco_entrega.place( x=73.0, y=215.0, width=137.0, height=29.325258255004883)

#entrada apartamento entrega
canvas.create_text( 239.0, 193.0, anchor="nw", text="apartamento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_apartamento_entrega = PhotoImage( file=relative_to_assets("entry_10.png"))
entry_bg_apartamento_entrega = canvas.create_image( 316.5, 230.66262912750244, image=entry_image_apartamento_entrega)
entry_apartamento_entrega = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_apartamento_entrega.place( x=248.0, y=215.0, width=137.0,  height=29.325258255004883)

#entrada data entrega
canvas.create_text( 64.0, 253.0, anchor="nw", text="data:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_data_entrega = PhotoImage( file=relative_to_assets("entry_7.png"))
entry_bg_data_entrega = canvas.create_image( 141.5, 290.66262912750244, image=entry_image_data_entrega)
entry_data_entrega = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_data_entrega.place( x=73.0, y=275.0, width=137.0, height=29.325258255004883)

#entrada porteiro entrega
canvas.create_text( 64.0, 310.0, anchor="nw", text="porteiro:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_porteiro_entrega = PhotoImage( file=relative_to_assets("entry_8.png"))
entry_bg_porteiro_entrega = canvas.create_image( 139.5, 347.66262912750244, image=entry_image_porteiro_entrega)
entry_porteiro_entrega = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_porteiro_entrega.place( x=71.0, y=332.0, width=137.0, height=29.325258255004883)

#button salvar
button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
button_1 = Button( image=button_image_1, borderwidth=0, highlightthickness=0, command=retirada, relief="flat")
button_1.place( x=562.0, y=437.0, width=77.0, height=34.890625)



preencher_entrega()

window.resizable(False, False)
window.mainloop()

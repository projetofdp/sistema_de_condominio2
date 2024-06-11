import sys
import os
import subprocess
from funcoesdb import * 
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, "..", "back", "banco_de_dados"))


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir, "assets", "frame5")

def voltar():
    args = [sys.executable, str(OUTPUT_PATH / "cadastro_moradores_i.py")]
    subprocess.run(args)

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)



def preencher_entradas_com_dados(nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento):
    entry_nome.insert(0, nome)
    entry_cpf.insert(0, cpf)
    entry_bloco.insert(0, placa_carro)
    entry_apartamento.insert(0, telefone)
    entry_placa_carro.insert(0, data_nascimento)
    entry_telefone.insert(0, apartamento)
    entry_data_nascimento.insert(0, bloco)

def editar_morador(nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento):
    try:
        resultado = editar_morador(nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento)
        
        if resultado:
            messagebox.showinfo("Sucesso", "Morador editado com sucesso.")
        else:
            messagebox.showerror("Erro", "Erro ao editar morador.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {e}")
def deletar_morador(): 
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    bloco = entry_bloco.get()
    apartamento = entry_apartamento.get()
    placa_carro = entry_placa_carro.get()
    telefone = entry_telefone.get()
    data_nascimento = entry_data_nascimento.get() 
    try:
        resultado = deletar_morador()
        
        if resultado:
            messagebox.showinfo("Sucesso", "Morador deletado com sucesso.")
        else:
            messagebox.showerror("Erro", "Erro ao deletar morador.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {e}")

def salvar_edicao():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    bloco = entry_bloco.get()
    apartamento = entry_apartamento.get()
    placa_carro = entry_placa_carro.get()
    telefone = entry_telefone.get()
    data_nascimento = entry_data_nascimento.get()
    
    editar_morador(nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento)

window = Tk()
window.geometry("950x680")
window.configure(bg="#FFFFFF")
window.title("Sistema de Condomínio")

canvas = Canvas(window, bg="#FFFFFF", height=680, width=950, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=salvar_edicao, relief="flat")
button_1.place(x=56.0, y=525.0, width=90.0, height=40.78125)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=deletar_morador, relief="flat")
button_2.place(x=169.0, y=526.0, width=90.0, height=37.82606506347656)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=voltar, relief="flat")
button_3.place(x=28.0, y=33.0, width=30.0, height=15.0)

canvas.create_text(683.0, 24.0, anchor="nw", text="cadastro de moradores", fill="#B9B9B9", font=("BeVietnamPro Light", 19 * -1))
canvas.create_text(58.0, 78.0, anchor="nw", text="Cadastro", fill="#8EBC4F", font=("BeVietnamPro Bold", 45 * -1))
canvas.create_text(58.0, 155.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))


entry_image_nome = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_nome = canvas.create_image(214.0, 192.66262912750244, image=entry_image_nome)
entry_nome = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_nome.place(x=67.0, y=177.0, width=294.0, height=29.325258255004883)

canvas.create_text(58.0, 214.0, anchor="nw", text="cpf:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))

entry_image_cpf = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_cpf = canvas.create_image(166.0, 251.66262912750244, image=entry_image_cpf)
entry_cpf = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_cpf.place(x=67.0, y=236.0, width=198.0, height=29.325258255004883)

canvas.create_text(56.0, 391.0, anchor="nw", text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_bloco = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_bloco = canvas.create_image(133.5, 428.66262912750244, image=entry_image_bloco)
entry_bloco = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_bloco.place(x=65.0, y=413.0, width=137.0, height=29.325258255004883)

canvas.create_text(231.0, 391.0, anchor="nw", text="apartamento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_apartamento = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_apartamento = canvas.create_image(308.5, 428.66262912750244, image=entry_image_apartamento)
entry_apartamento = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_apartamento.place(x=240.0, y=413.0, width=137.0, height=29.325258255004883)

canvas.create_text(56.0, 450.0, anchor="nw", text="placa do carro:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_placa_carro = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_placa_carro = canvas.create_image(133.5, 487.66262912750244, image=entry_image_placa_carro)
entry_placa_carro = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_placa_carro.place(x=65.0, y=472.0, width=137.0, height=29.325258255004883)


canvas.create_text(58.0, 332.0, anchor="nw", text="telefone:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_telefone = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_telefone = canvas.create_image(164.0, 369.66262912750244, image=entry_image_telefone)
entry_telefone = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_telefone.place(x=65.0, y=354.0, width=228.0, height=29.325258255004883)

canvas.create_text(58.0, 273.0, anchor="nw", text="data de nascimento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_data_nascimento = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_data_nascimento = canvas.create_image(164.0, 310.66262912750244, image=entry_image_data_nascimento)
entry_data_nascimento = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_data_nascimento.place(x=65.0, y=295.0, width=198.0, height=29.325258255004883)

dados = sys.argv[1:]

if len(dados) == 7:
    nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento = dados
    preencher_entradas_com_dados(nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento)


window.resizable(False, False)
window.mainloop()



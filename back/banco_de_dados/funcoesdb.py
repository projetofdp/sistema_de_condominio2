from .validar_entry import (
    validar_nome, 
    validar_cpf, 
    validar_telefone,  
    validar_data_nascimento, 
    validar_bloco, 
    validar_apartamento, 
    validar_placa_carro
)


import sqlite3
from tkinter import messagebox



def inserir_morador(nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro):

    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "CPF inválido. Deve conter exatamente 11 números.")
        return
    if not validar_telefone(telefone):
        messagebox.showerror("Erro", "Telefone inválido. Deve conter exatamente 11 números.")
        return
    if not validar_data_nascimento(data_nascimento):
        messagebox.showerror("Erro", "Data de nascimento inválida. Deve estar no formato DDMMAAAA.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return
    if not validar_placa_carro(placa_carro):
        messagebox.showerror("Erro", "Placa de Carro inválida. Deve conter 7 caracteres alfanuméricos.")
        return
    

    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO moradores (nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", "Morador inserido com sucesso.")

def inserir_visitante(nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    
    # Obtendo o morador_id baseado em nome, bloco e apartamento
    cursor.execute('''
    SELECT id FROM moradores
    WHERE nome = ? AND bloco = ? AND apartamento = ?
    ''', (nome_morador, bloco, apartamento))
    morador = cursor.fetchone()
    
    if morador:
        morador_id = morador[0]
        cursor.execute('''
        INSERT INTO visitantes (morador_id, nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (morador_id, nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento))
        conn.commit()
    else:
        print("Morador não encontrado.")
    
    conn.close()


def pesquisar_morador(nome, bloco, apartamento):
    conexao = sqlite3.connect('condominio.db')
    cursor = conexao.cursor()
    query = "SELECT * FROM moradores WHERE nome = ? AND bloco = ? AND apartamento = ?"
    cursor.execute(query, (nome, bloco, apartamento))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado

import sqlite3
from tkinter import messagebox

def inserir_encomenda(nome, data_entrega, bloco, apartamento, porteiro):
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_data_nascimento(data_entrega):
        messagebox.showerror("Erro", "Data de entrega inválida. Deve estar no formato DDMMAAAA.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return
    if not validar_nome(porteiro):
        messagebox.showerror("Erro", "Nome do porteiro inválido. Deve conter apenas letras e até 50 caracteres.")
        return

    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO encomendas (nome, data_entrega, bloco, apartamento, porteiro)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, data_entrega, bloco, apartamento, porteiro))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", "Encomenda inserida com sucesso.")

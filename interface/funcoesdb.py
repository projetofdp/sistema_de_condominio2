from validar_entry import *


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
    query ="SELECT nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro FROM moradores WHERE nome = ? AND bloco = ? AND apartamento = ?"
    cursor.execute(query, (nome, bloco, apartamento))
    dados = cursor.fetchone()
    conexao.close()
    return dados



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


def inserir_informacoes_encomendas(nome_de_quem_retirou, cpf, data_retirada):
    # Conectar ao banco de dados
    conn = sqlite3.connect('encomendas.db')
    cursor = conn.cursor()

    # Inserir informações na tabela
    cursor.execute('''
        INSERT INTO encomenda (nome_de_quem_retirou, cpf, data_retirada)
        VALUES (?, ?, ?)
    ''', (nome_de_quem_retirou, cpf, data_retirada))

    # Commit e fechar conexão
    conn.commit()
    conn.close()

def editar_morador(nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro):
    try:
        # Conectar-se ao banco de dados
        conn = sqlite3.connect("condominio.db")
        cursor = conn.cursor()

        # Query SQL para atualizar os dados do morador
        query = """
            UPDATE moradores
            SET nome = ?, cpf = ?, data_nascimento = ?, telefone = ?, bloco = ?, apartamento = ?, placa_carro = ?
        """

        # Executar a query SQL
        cursor.execute(query, (nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro))
        
        # Commit para salvar as alterações
        conn.commit()

        # Fechar a conexão com o banco de dados
        cursor.close()
        conn.close()

        return True  # Retorna True se a edição for bem-sucedida
    except sqlite3.Error as e:
        print("Erro ao editar morador:", e)
        return False  # Retorna False se ocorrer algum erro
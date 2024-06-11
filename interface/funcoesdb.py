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
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return
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
    INSERT INTO encomenda (nome, data_entrega, bloco, apartamento, porteiro)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, data_entrega, bloco, apartamento, porteiro))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", "Encomenda inserida com sucesso.")


def inserir_informacoes_encomendas(id_, nome_de_quem_retirou, cpf, data_retirada):
    # Conectar ao banco de dados
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()

    # Inserir informações na tabela
    cursor.execute('''
        UPDATE encomenda 
        SET nome_de_quem_retirou = ?, cpf = ?, data_retirada = ? 
        WHERE id = ?
    ''', (nome_de_quem_retirou, cpf, data_retirada, id_))

    # Commit e fechar conexão
    conn.commit()
    conn.close()

def editar_morador(nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro):
    try:
        # Conectar-se ao banco de dados
        conn = sqlite3.connect("condominio.db")
        cursor = conn.cursor()

        # Query SQL para atualizar os dados do morador
        # Atualize as informações do morador no banco de dados
        cursor.execute("""
            UPDATE moradores SET 
                nome = ?, 
                bloco = ?, 
                apartamento = ?, 
                placa_carro = ?, 
                telefone = ?, 
                data_nascimento = ?
            WHERE cpf = ?
        """, (nome, bloco, apartamento, placa_carro, telefone, data_nascimento, cpf))
        
        conn.commit()
        affected_rows = cursor.rowcount
        conn.close()
        
        return affected_rows > 0  # Retorna True se alguma linha foi afetada, caso contrário False
    except sqlite3.Error as e:
        print(f"Erro de banco de dados: {e}")
        raise e
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise e
    
def deletar_morador():
    try:
        conn = sqlite3.connect('condominio.db')
        cursor = conn.cursor()

        # Deleta todas as informações dos moradores no banco de dados
        cursor.execute("""
            DELETE FROM moradores 
            WHERE nome = ? AND cpf = ? AND bloco = ? AND apartamento = ? AND placa_carro = ? AND telefone = ? AND data_nascimento = ?
        """, (nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento))
        
        conn.commit()
        affected_rows = cursor.rowcount
        conn.close()
        
        return affected_rows > 0  # Retorna True se alguma linha foi afetada, caso contrário False
    except sqlite3.Error as e:
        print(f"Erro de banco de dados: {e}")
        raise e
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise e
    
def pesquisar_encomenda(nome, bloco, apartamento):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nome, bloco, apartamento, porteiro, data_entrega, id
        FROM encomenda
        WHERE nome = ? AND bloco = ? AND apartamento = ?
        ORDER BY data_entrega ASC
    """, (nome, bloco, apartamento))  # Forneça os três valores aqui
    dados_encomenda = cursor.fetchall()
    conn.close()
    return dados_encomenda

def buscar_visitantes(nome_morador):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT nome_visitante, horario1, horario2, data
    FROM visitantes
    WHERE nome_morador = ?
    ''', (nome_morador,))
    visitantes = cursor.fetchall()
    conn.close()
    return visitantes


def pesquisar_encomenda_antigas(nome, bloco, apartamento):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM encomendas_antigas
        WHERE nome = ? AND bloco = ? AND apartamento = ?
        ORDER BY data_entrega ASC
        """, (nome, bloco, apartamento))# Forneça os três valores aqui
    dados_encomenda_antigas = cursor.fetchall()
    conn.close()
    return dados_encomenda_antigas


def inserir_informacoes_encomendas_antigas(nome, apartamento, bloco, data_entrega, data_retirada, porteiro, cpf, nome_de_quem_retirou):
    # Conectar ao banco de dados
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    
    # Criar um cursor para executar consultas SQL
    cursor = conn.cursor()
    
    # Inserir os dados na tabela encomenda_antigas
    cursor.execute('''INSERT INTO encomenda_antigas (nome, apartamento, bloco, data_entrega, data_retirada, porteiro, cpf, nome_de_quem_retirou)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (nome, apartamento, bloco, data_entrega, data_retirada, porteiro, cpf, nome_de_quem_retirou))
    
    # Commit para salvar as alterações no banco de dados
    conn.commit()
    
    # Fechar a conexão com o banco de dados
    conn.close()

def apagar_dados_outra_tabela(id_):
    # Conectar ao banco de dados
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    
    # Criar um cursor para executar consultas SQL
    cursor = conn.cursor()
    
    # Inserir os dados na tabela encomenda_antigas
    cursor.execute('''DELETE FROM encomenda WHERE id = ?''', (id_,))
    # Commit para salvar as alterações no banco de dados
    conn.commit()
    
    # Fechar a conexão com o banco de dados
    conn.close()

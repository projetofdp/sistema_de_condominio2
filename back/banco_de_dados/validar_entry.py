import re

def validar_nome(nome):
    match = re.match(r'^[a-zA-Z\s]{1,50}$', nome)
    return match is not None

# Função para validar CPF
def validar_cpf(cpf):
    match = re.match(r'^\d{11}$', cpf) 
    return match is not None

# Função para validar telefone
def validar_telefone(telefone):
    match = re.match(r'^\d{11}$', telefone)
    return match is not None

def validar_data_nascimento(data_nascimento):
    match = re.match(r'^\d{8}$', data_nascimento)
    return match is not None

def validar_bloco(bloco):
    match = re.match(r'^[a-zA-Z\s]{1}$', bloco)
    return match is not None

def validar_apartamento(apartamento):
    match = re.match(r'^\d{3}$', apartamento)
    return match is not None

def validar_placa_carro(placa_carro):
    match = re.match(r'^[a-zA-Z0-9\s]{1,50}$', placa_carro)
    return match is not None
    
def validar_porteiro(porteiro):
    match = re.match(r'^[a-zA-Z\s]{1,50}$', porteiro)
    return match is not None

def validar_data_entrega(data_entrega):
    match = re.match(r'^\d{8}$', data_entrega)
    return match is not None

def validar_data_retirada(data_retirada):
    match = re.match(r'^\d{8}$', data_retirada)
    return match is not None
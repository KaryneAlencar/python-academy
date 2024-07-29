def login_disponivel(loguin, lista):
    if loguin not in lista:
        return loguin
    
    numero = 1
    while f'{loguin}{numero}' in lista:
        numero += 1
    return f'{loguin}{numero}'
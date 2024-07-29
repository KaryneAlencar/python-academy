def valida_senha(senha):
    print(senha)
    especial = ['?', '!', '@', '#', '$', '%', '&', '*']

    if len(senha) < 8:
        return False
    
    for i in range(len(senha)-1):
        if senha[i] == senha[i+1]:
            return False
    
    especiais_encontrados = ''
    for letra in senha:
        if letra in especial:
            if letra not in especiais_encontrados:
                especiais_encontrados += letra
    if len(especiais_encontrados) < 2:
        return False
    
    return True
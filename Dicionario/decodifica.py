def decodifica(string, troca_sistema):
    troca_invertida = {}
    for chave, valor in troca_sistema.items():
        troca_invertida[valor] = chave
    
    decodificado = ''
    
    for letra in string:
        if letra in troca_invertida:
            decodificado += troca_invertida[letra]
        else:
            decodificado += letra
    
    return decodificado

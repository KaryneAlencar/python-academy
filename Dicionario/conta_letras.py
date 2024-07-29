def conta_letras(string):
    contagem = {}
    for letra in string:
        if letra not in contagem:
            contagem[letra] = 1
        else:
            contagem[letra] += 1
    return contagem
def conta_bigramas(string):
    contagem = {}
    for i in range(len(string)-1):
        bigrama = string[i] + string[i+1]
        if bigrama not in contagem:
            contagem[bigrama] = 1
        else:
            contagem[bigrama] += 1
    return contagem
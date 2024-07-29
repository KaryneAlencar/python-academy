def soma_valores(lista):
    soma = 0
    i = 0
    while i < len(lista):
        termo = lista[i]
        soma += termo
        i += 1
    return soma
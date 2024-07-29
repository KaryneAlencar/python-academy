def soma_pecas(lista_pecas):
    soma = 0
    for elemento in lista_pecas:
        for numero in elemento:
            soma += numero
    return soma
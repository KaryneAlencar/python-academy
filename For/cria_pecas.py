import random
def cria_pecas():
    lista = []
    for i in range(0, 7):
        for j in range(0, 7):
            if not [j,i] in lista:
                lista.append([j,i])
    random.shuffle(lista)
    return lista
def adiciona_em_ordem(pais,distancia, lista):
    if pais in lista:
        return lista
    i = 0
    for i in range(len(lista)):
        if lista[i][1] >= distancia:
            break
    lista.insert(i, [pais, distancia])
    return lista
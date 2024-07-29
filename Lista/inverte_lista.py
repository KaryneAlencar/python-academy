def inverte_lista(lista):
    lista_invertida = []
    i = len(lista)-1
    while i >= 0:
        lista_invertida.append(lista[i])
        i -= 1
    return lista_invertida
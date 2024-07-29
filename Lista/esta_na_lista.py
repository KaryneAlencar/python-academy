def esta_na_lista(pais, lista):
    tam = len(lista)
    i = 0
    while i < tam:
        if lista[i][0] == pais:
            return True
        i += 1
    return False
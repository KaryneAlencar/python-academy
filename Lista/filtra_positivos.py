def filtra_positivos(lista_reais):
    lista_positivos = []

    i = 0
    while i < len(lista_reais):
        if lista_reais[i] > 0:
            lista_positivos.append(lista_reais[i])
        i += 1
    return lista_positivos
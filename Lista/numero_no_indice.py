def numero_no_indice(lista_n):
    lista_igual = []
    i = 0
    while i < len(lista_n):
        if i == lista_n[i]:
            lista_igual.append(lista_n[i])
        i += 1
    return lista_igual
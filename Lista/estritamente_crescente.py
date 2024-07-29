def estritamente_crescente(lista_n):
    if not lista_n:
        return []
    lista_crescente = []
    lista_crescente.append(lista_n[0])
    for i in lista_n:
        if i > lista_crescente[-1]:
            lista_crescente.append(i)
    return lista_crescente
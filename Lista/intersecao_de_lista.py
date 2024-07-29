def intersecao_de_lista(lista1, lista2):
    lista_intersecao = []
    for i in lista1:
        if i in lista2:
            lista_intersecao.append(i)
    return lista_intersecao
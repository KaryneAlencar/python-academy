def junta_nome_sobrenome(lista_nomes, lista_sobrenomes):
    lista_completa = []
    i = 0
    while i < len(lista_nomes):
        lista_completa.append(lista_nomes[i] + ' ' + lista_sobrenomes[i])
        i += 1
    return lista_completa
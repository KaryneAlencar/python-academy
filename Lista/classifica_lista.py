def classifica_lista(lista_n):
    if len(lista_n) < 2:
        return 'nenhum'
    
    decrescente = False
    crescente = False
    for i in range(1, len(lista_n)): #evita acessar o -1, ultimo elemento
        if lista_n[i] > lista_n[i-1]:
            crescente = True
        elif lista_n[i] < lista_n[i-1]:
            decrescente = True
    if crescente and decrescente:
        return 'nenhum'
    elif crescente:
        return 'crescente'
    elif decrescente:
        return 'decrescente'
    else:
        return 'nenhum'
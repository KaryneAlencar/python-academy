def nomes_com_vogais(lista_nomes):
    lista_contagem = [0,0]

    vogais = ['A', 'E', 'I', 'O', 'U']

    for nome in lista_nomes:
            if nome[0] in vogais:
                lista_contagem[0] += 1
            else:
                lista_contagem[1] += 1

    return lista_contagem
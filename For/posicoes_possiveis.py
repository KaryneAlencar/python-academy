def posicoes_possiveis (lista_mesa, lista_pecas):
    possiveis = []
    esquerdo = lista_mesa[0][0]
    direito = lista_mesa[-1][1]

    for i in range(len(lista_pecas)):
        for peca in lista_pecas[i]:
            if peca[0] == esquerdo or peca[1] == esquerdo or peca[0] == direito or peca[1] == direito: 

                possiveis.append(i)
    return possiveis
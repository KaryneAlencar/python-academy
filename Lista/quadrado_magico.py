def quadrado_magico(matriz):
    soma_padrao = 0
    for numero in matriz[0]:
        soma_padrao += numero

    for linha in matriz:
        soma_linha = 0 #dessa forma a soma reinicia quando for fazer a soma de uma nova linha
        for numero in linha:
            soma_linha += numero
        if soma_linha != soma_padrao:
            return False

    for coluna in range(len(matriz)): #ela pega o indice e se guia por ele, para 'formar' a coluna'
        soma_coluna = 0
        for linha in matriz:
            soma_coluna += linha[coluna]
        if soma_coluna != soma_padrao:
            return False

    diagonal1 = 0
    for i in range(len(matriz)):
        diagonal1 += matriz[i][i]
    if diagonal1 != soma_padrao:
        return False

    diagonal2 = 0
    for i in range(len(matriz)):
        diagonal2 += matriz[i][len(matriz) - 1 - i]
    if diagonal2 != soma_padrao:
        return False

    return True
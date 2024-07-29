def eh_identidade(matriz):
    #verifica se a matriz é quadrada
    qnt_linha = 0
    qnt_n = 0
    for linha in matriz:
        qnt_linha += 1
        for n in linha:
            qnt_n += 1
    if qnt_linha != (qnt_n/qnt_linha):
        return False

    # Verifica identidade
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                if matriz[i][j] != 1:
                    return False
            else:
                if matriz[i][j] != 0:
                    return False
    return True
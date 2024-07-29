def encontra_maximo(matriz):
    maior_valor = 0
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            if abs(matriz[i][j]) > maior_valor:
                maior_valor = abs(matriz[i][j])
            j += 1
        i += 1
    return maior_valor
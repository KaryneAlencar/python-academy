def contabilizar(volume_padrao, lista):#lista[volume, quantas vezes foi enchida]
    volume_usado = 0
    for i in lista:
        volume_usado += i[0]*i[1]

    garrafas_economizadas = volume_usado//volume_padrao
    return garrafas_economizadas
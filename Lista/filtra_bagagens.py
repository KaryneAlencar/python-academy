def filtra_bagagens(lista_bagagens, altura, largura, profundidade):
    bagagem_irregular = 0
    for bagagem in lista_bagagens:
        if bagagem[0] > altura or bagagem[1] > largura or bagagem[2] > profundidade:
            bagagem_irregular += 1
    return bagagem_irregular 
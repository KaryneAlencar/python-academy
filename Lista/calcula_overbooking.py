def calcula_overbooking(capacidade, lista_venda):
    overbooking = 0
    i = 0
    while i < len(lista_venda):
        if lista_venda[i] > capacidade:
            overbooking += lista_venda[i] - capacidade #soma a quantidade que excedeu sempre que tiver overbooking, e assim atualiza a variável
        i += 1
    
    return overbooking
#usando for
    overbooking = 0
    for venda in lista_venda:
        if venda > capacidade:
            overbooking += venda - capacidade
    return overbooking
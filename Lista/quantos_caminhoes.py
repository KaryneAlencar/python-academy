def quantos_caminhoes(lista_peso):
    caminhoes = 0
    peso = 0
    i = 0

    while i < len(lista_peso):
        if peso + lista_peso[i] > 2000: #enquanto o caminhão não chegar a 2000 ele nn contabiliza +1
            caminhoes += 1
            peso = lista_peso[i] #reinicia o peso
        else:
            peso += lista_peso[i] #vai add peo, até dar 2000 para contabilizar um caminhão
        
        i += 1
    
    if peso > 0:
        caminhoes += 1
    
    return caminhoes
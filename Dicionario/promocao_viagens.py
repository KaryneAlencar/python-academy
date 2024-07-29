def promocao_viagens(destinos):
    destinos_promocao = {}
    for destino, lista in destinos.items():
        if lista[0] == 1:
            preco = lista[1]*0.9
        if lista[0] == 2:
            preco = lista[1]*0.8
        if lista[0] == 3:
            preco = lista[1]*0.7
        if lista[0] == 4:
            preco = lista[1]*0.6
        if lista[0] == 5:
            preco = lista[1]*0.5
        
        destinos_promocao[destino] = preco #nn tem append
    return destinos_promocao
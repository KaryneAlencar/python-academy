def classifica_trigo(lista_trigo):
    classifica = []
    for trigo in lista_trigo:
        if trigo <= 2:
            classifica.append('T1')
        elif trigo <= 3:
            classifica.append('T2')
        elif trigo <= 7:
            classifica.append('T3')
        else:
            classifica.append('FT')
    return classifica
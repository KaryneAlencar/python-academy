def organiza_filas(lista_corredores):
    fila1 = []
    fila2 = []
    fila3 = []
    fila4 = []
    lista_final = []
    for corredor in lista_corredores:
        if corredor[1] <= 20:
            fila1.append(corredor[0])
        elif corredor[1] <= 40:
            fila2.append(corredor[0])
        elif corredor[1] <= 60:
            fila3.append(corredor[0])
        else:
            fila4.append(corredor[0])
    lista_final.append(fila1)
    lista_final.append(fila2)
    lista_final.append(fila3)
    lista_final.append(fila4)
    return lista_final
    

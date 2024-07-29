def maior_abobora(especie, lista_aboboras):
    maior_abobora = 0
    indice = -1
    for i in range(len(lista_aboboras)):
        for abobora in lista_aboboras[i]:
            if abobora[1] == especie:
                if abobora[0] > maior_abobora:
                    maior_abobora = abobora[0]
                    indice = i
    return indice
def maior_abobora(especie, lista_aboboras):
    maior_abobora = 0
    indice = -1 #inicializa o indice
    i = 0 # o i vai ser o indice
    while i < len(lista_aboboras): #pega o indice
        for abobora in lista_aboboras[i]:
            if abobora[1] == especie:
                if abobora[0] > maior_abobora:
                    maior_abobora = abobora[0]
                    indice = i
        i += 1
    return indice
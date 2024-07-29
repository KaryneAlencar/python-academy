def calcula_escola(lista_notas):
    print(lista_notas)
    #criar lista com todas as menores notas de cada quesito
    lista_menor_nota = []
    menor_nota = float('inf')
    for quesito in lista_notas:
        for nota in range(len(quesito)):
            if quesito[nota] < menor_nota:
                menor_nota = quesito[nota]
        lista_menor_nota.append(menor_nota)
        menor_nota = float('inf') #'zera' a menor nora, pois irá iniciara a comparação de um novo quesito

    #soma todas as notas    
    soma_notas = 0
    for quesito in lista_notas:
        for nota in quesito:
            soma_notas += nota

    #soma todas as menores notas
    soma_menor_nota = 0
    for nota in lista_menor_nota:
        soma_menor_nota += nota
        
    #subtrai
    nota_final = soma_notas - soma_menor_nota
    return nota_final


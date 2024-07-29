def medias_por_inicial(dic_notas):
    dic_iniciais_notas = {}

    for nome, nota in dic_notas.items():
        if nome[0] in dic_iniciais_notas:
            dic_iniciais_notas[nome[0]].append(nota)
        else:
            dic_iniciais_notas[nome[0]] = [nota]
    
    dic_medias = {}
    for inicial, lista_notas in dic_iniciais_notas.items():
        total = 0
        for nota in lista_notas:
            total += nota
        dic_medias[inicial] = total / len(lista_notas)
    return dic_medias
    
    
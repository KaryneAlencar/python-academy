def seleciona_candidatos(lista_candidato, lista_criterios):
    lista_aprovados = []
    for candidato in lista_candidato:
        if len(candidato[2]) == 3:
            if candidato[2][0] >= lista_criterios[0] and candidato[2][1] >= lista_criterios[1] and candidato[2][2] >= lista_criterios[2]:
                        lista_aprovados.append([candidato[0],candidato[1]])
    return lista_aprovados


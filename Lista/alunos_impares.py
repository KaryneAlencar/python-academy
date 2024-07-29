def alunos_impares(lista_alunos):
    al_impar = []
    i = 1
    while i < len(lista_alunos):
        al_impar.append(lista_alunos[i])
        i += 2
    return al_impar
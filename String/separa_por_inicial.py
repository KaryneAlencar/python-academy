def separa_por_inicial(dic_turmas):
    dic_nomes = {}
    for alunos in dic_turmas.values(): #alunos é uma lista
        for aluno in alunos:
            inicial = aluno[0]
            if inicial in dic_nomes:
                dic_nomes[inicial].append(aluno)
            else:
                dic_nomes[inicial] = aluno
    return dic_nomes
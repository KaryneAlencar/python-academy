def calcula_estado(matriz_alunos):
    lista_estado = []
    for aluno in matriz_alunos:
        soma_nota = 0
        menor_nota = float('inf')
        for nota in aluno[1]:
            soma_nota += nota
            if nota < menor_nota:
                menor_nota = nota
        nota_quiz = ((soma_nota - menor_nota)/4)*0.1
        ai = aluno[2][0]
        nota_ai = ai*0.4
        pf = aluno[2][1]
        nota_pf = pf*0.5
        media = nota_ai +nota_pf +nota_quiz
        if media >= 5:
            lista_estado.append([aluno[0],'A'])
        else:
            lista_estado.append([aluno[0],'R'])
    return lista_estado


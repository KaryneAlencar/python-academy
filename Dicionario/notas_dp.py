def notas_dp(notas):
    lista_dp = []
    for aluno in notas:
        media = (aluno['PI'] + aluno['PF'])/2

        if media < 5:
            lista_dp.append(aluno['matricula'])
    
    return lista_dp
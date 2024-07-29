def calcula_media(lista):
    soma = 0
    alunos = 0
    for dict in lista:
        for nota in dict.values():
            soma += nota
            alunos += 1
    media = soma/alunos
    return media

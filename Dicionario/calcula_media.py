def calcula_media(dic_atletas, pais):
    soma = 0
    qnt = 0

    for infos in dic_atletas.values():
        idade = infos['idade']
        nacionalidade = infos['nacionalidade']

        if nacionalidade == pais:
            soma += idade
            qnt += 1
    
    media = soma / qnt
    return media
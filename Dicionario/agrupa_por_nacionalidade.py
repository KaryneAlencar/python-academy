def agrupa_por_nacionalidade(dic_atleta):
    dic_nacionalidade = {}

    for atleta, infos in dic_atleta.items():
        pais = infos['nacionalidade']

        if pais not in dic_nacionalidade:
            dic_nacionalidade[pais] = [atleta]
        else:
            dic_nacionalidade[pais].append(atleta)
    return dic_nacionalidade
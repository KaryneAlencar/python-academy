def interseccao_chaves(dic1, dic2):
    chaves_comuns = []
    for chave in dic1.keys():
        if chave in dic2:
            chaves_comuns.append(chave)
    return chaves_comuns

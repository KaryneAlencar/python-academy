def dias_de_racao(lista_estoque, dic_pet):
    idade = dic_pet['idade']
    gramas_dia = dic_pet['gramas_dia']
    porte = dic_pet['porte']

    if idade <= 1:
        classificacao = 'filhote'
    elif idade >1 and idade < 8:
        classificacao = 'adulto'
    else:
        classificacao = 'idoso'

    duracao = 0
    kg_total = 0
    for dic_racao in lista_estoque:
            if dic_racao['porte'] == porte and dic_racao['indicado'] == classificacao:
                kg_total += dic_racao['qtde']*1000
                duracao = kg_total//gramas_dia             
    return duracao

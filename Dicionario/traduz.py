def traduz(lista_ingles, dic_traducao):
    lista_traducao = []
    for palavra in lista_ingles:
        traducao = dic_traducao[palavra]
        lista_traducao.append(traducao)
    return lista_traducao
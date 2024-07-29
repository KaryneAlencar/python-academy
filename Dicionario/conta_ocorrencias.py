def conta_ocorrencias(lista_palavras):
    ocorrencias = {}
    for palavra in lista_palavras:
        if palavra in ocorrencias:
            ocorrencias[palavra] += 1
        else:
            ocorrencias[palavra] = 1
    return ocorrencias
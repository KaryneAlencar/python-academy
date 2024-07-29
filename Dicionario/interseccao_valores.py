def interseccao_valores(dic1, dic2):
    valores_comuns = []
    for valores in dic1.values():
        if valores in dic2.values():
            valores_comuns.append(valores)
    return valores_comuns

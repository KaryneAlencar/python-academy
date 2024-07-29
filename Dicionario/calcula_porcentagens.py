def calcula_porcentagens(dict_resultados):
    erros = {}
    total = 0
    
    for v in dict_resultados.values():
        total += v

    for k, v in dict_resultados.items():
        erros[k] = (v*100)/total
    return erros

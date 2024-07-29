def calcula_idade(d, m, a, dp, mp, ap):
    #legenda
    # d = dia, m = mês, a = ano, dp = dia posterior, mp = mês posterios, ap = ano posterior
    idade = ap - a
    if mp < m or (m == mp and dp < d):
        idade -= 1
    return idade
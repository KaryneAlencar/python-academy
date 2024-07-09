def calcula_investimento(inicial, meses, ativo):
    rendimento_mensal = 0
    bonus = 0
    if ativo == 'CDB':
        rendimento_mensal = 0.013
        bonus = 0.012 # a cada 6 meses
    if ativo == 'LCI':
        rendimento_mensal = 0.016
    if ativo == 'LCA':
        rendimento_mensal = 0.0145
        bonus = 0.01 # a cada 4 meses

    total = inicial
    mes = 1
    while mes <= meses:
        total = total + (total * rendimento_mensal)
        if bonus != 0:
            if ativo == 'CDB' and mes % 6 == 0:
                total = total + (total * bonus)
            elif ativo == 'LCA' and mes % 4 == 0:
                total = total + (total * bonus)
        mes += 1 
    return total
def total_centro_custo(dic_gastos):
    dic_total_gastos = {}
    
    for trabalhador, info in dic_gastos.items():
        local = info['centro de custo']
        valor = info['valor']
        if local in dic_total_gastos:
            if local == 'tesouraria':
                dic_total_gastos['tesouraria'] += valor
            if local == 'presidencia':
                dic_total_gastos['presidencia'] += valor
            if local == 'producao':
                dic_total_gastos['producao'] += valor
        else:
            dic_total_gastos[local] = valor
    return dic_total_gastos
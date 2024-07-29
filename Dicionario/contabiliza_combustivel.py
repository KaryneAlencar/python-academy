def contabiliza_combustivel(dic_combustivel):
    resultado = {}
    for info in dic_combustivel.values():
        tipo = info['tipo']
        litros = info['litros']
        custo = info['custo']

        if tipo not in resultado:
            resultado[tipo] = {'total litros': 0, 'custo total': 0.0}

        resultado[tipo]['total litros'] += litros
        resultado[tipo]['custo total'] += custo


    for tipo, info in resultado.items():
        total_litros = info['total litros']
        custo_total = info['custo total']
        custo_por_litro = custo_total/total_litros
        resultado[tipo] = {'total litros': total_litros, 'custo por litro': custo_por_litro}
    return resultado
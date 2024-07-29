def monitora_represas(dic_estado_inicial, dic_variacoes):
    dic_classificacao = {}

    for represa, dados in dic_estado_inicial.items():
        capacidade = dados['capacidade']
        volume_atual_percent = dados['volume']
        volume_atual_litros = volume_atual_percent / 100 * capacidade

        for dia, (precipitacao, consumo) in dic_variacoes[represa].items():
            volume_atual_litros += precipitacao
            volume_atual_litros -= consumo
            if volume_atual_litros < 0:
                volume_atual_litros = 0

        v_final = (volume_atual_litros / capacidade) * 100

        if v_final < 20:
            classificacao = 'emergencia'
        elif 20 <= v_final < 50:
            classificacao = 'critico'
        elif 50 <= v_final < 70:
            classificacao = 'atencao'
        elif 70 <= v_final <= 100:
            classificacao = 'normal'
        else:
            classificacao = 'escoar'

        if classificacao not in dic_classificacao:
            dic_classificacao[classificacao] = []

        dic_classificacao[classificacao].append(represa)

    return dic_classificacao
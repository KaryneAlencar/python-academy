def converte_receita(dic_resceita):
    conversao = {
        "xícaras": 250,
        "xícara": 250,
        "colheres de sopa": 15,
        "colher de sopa": 15,
        "colheres de chá": 5,
        "colher de chá": 5
    }
    dic_conversao = {}

    for ingrediente, quantidade in dic_resceita.items():
        partes = quantidade.split()
        if len(partes) == 2:
            valor = int(partes[0])
            unidade = partes[1]

            if unidade in conversao:
                qnt_ml = valor*conversao[unidade]
                dic_conversao[ingrediente] = f'{qnt_ml} ml'
            else:
                dic_conversao[ingrediente] = quantidade
        else:
            dic_conversao[ingrediente] = quantidade
    return dic_conversao
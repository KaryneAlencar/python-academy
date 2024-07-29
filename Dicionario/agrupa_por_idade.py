def agrupa_por_idade(dic_pessoas):
    dic_etario = {
        'criança': [], 
        'adolescente': [], 
        'adulto': [],
        'idoso': []
    }

    for nome, idade in dic_pessoas.items():
        if idade <= 11:
            dic_etario['criança'].append(nome)
        elif idade >= 12 and idade <= 17:
            dic_etario['adolescente'].append(nome)
        elif idade >= 18 and idade <= 59:
            dic_etario['adulto'].append(nome)
        else:
            dic_etario['idoso'].append(nome)
    return dic_etario 
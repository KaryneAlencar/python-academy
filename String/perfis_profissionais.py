def perfis_profissionais(dic_proficionais):
    dic_censo = {}

    for pessoas, infos in dic_proficionais.itens():
        ramo = infos['ramo']
        salario = infos['salario']
        anos_serviços = infos['anos de serviço']
        email = infos['e-mail']
        servidores = email.split('@')[1].split('.')[0]
        
        if ramo not in dic_censo:
            dic_censo[ramo] = {
                'média salarial': 0,
                'tempo médio de serviço': 0,
                'servidores': [],
                'total_salario': 0,
                'total_anos_servico': 0,
                'num_pessoas': 0
            }
            
        dic_censo[ramo]['total_salario'] += salario
        dic_censo[ramo]['total_anos_servico'] += anos_serviços
        dic_censo[ramo]['numero_pessoas'] += 1

        if servidores not in dic_censo[ramo]['servidores']:
            dic_censo[ramo]['servidores'].append(servidores)
        
        for ramo, infos in dic_censo.items():
            infos['média salarial'] = infos['total_salario'] // infos['num_pessoas']
            infos['tempo médio de serviço'] = infos['total_anos_servico'] // infos['num_pessoas']
            del infos['total_salario']
            del infos['total_anos_servico']
            del infos['num_pessoas']
    
    return dic_censo


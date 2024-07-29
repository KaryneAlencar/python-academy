def calcula_dano(dic_heroi):
    danos = 0
    danos += dic_heroi['força']
    if len(dic_heroi['equipamentos']) != 0:
        for equipamento in dic_heroi['equipamentos']:
            danos += equipamento['força']
    return danos
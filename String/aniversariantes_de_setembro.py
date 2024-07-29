def aniversariantes_de_setembro(dic_anv):
    aniversarios = {}

    for nome, data in dic_anv.items():
        data_separa = data.split('/')
        mes = data_separa[1]

        if mes == '09':
            aniversarios[nome] = data
    return aniversarios

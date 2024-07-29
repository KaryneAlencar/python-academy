def calcula_idade(data_nascimento, data_posterior):
    print(data_nascimento)
    print(data_posterior)
    nasc = data_nascimento.split('/')
    pos = data_posterior.split('/')

    ano_nasc = int(nasc[2])
    mes_nasc = int(nasc[1])
    dia_nasc = int(nasc[0])
    
    ano_pos = int(pos[2])
    mes_pos = int(pos[1])
    dia_pos = int(pos[0])


    idade = ano_pos - ano_nasc

    if (mes_pos < mes_nasc) or (mes_pos == mes_nasc and dia_pos < dia_nasc):
        idade -= 1

    return idade
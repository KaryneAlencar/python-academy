def nivel_idh(idh):
    if 0.800 <= idh <= 1.000:
        return 'Muito Alto'
    elif 0.700 <= idh < 0.800:
        return 'Alto'
    elif 0.555 <= idh < 0.700:
        return 'Médio'
    elif 0.350 <= idh < 0.555:
        return 'Baixo'
    else:
        return 'Sem dados'
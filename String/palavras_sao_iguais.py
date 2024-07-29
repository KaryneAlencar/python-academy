def palavras_sao_iguais(string):
    partes = string.split('-')
    if len(partes) == 2 and partes[0] == partes[1]:
        return True
    else:
        return False
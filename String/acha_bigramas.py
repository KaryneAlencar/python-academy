def acha_bigramas(string):
    bigramas = []
    for i in range(len(string)-1):
        bigrama =string[i:i+2]
        if bigrama not in bigramas:
            bigramas.append(bigrama)
    return bigramas
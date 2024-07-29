def primeiras_ocorrencias(string):
    ocorrencias = {}
    indice = 0
    for caractere in string:
        if caractere not in ocorrencias:
            ocorrencias[caractere] = indice
        indice += 1
    return ocorrencias
def apaga_repetidos(string):
    ocorrencias = [] #lista com as letras que ja apareceram
    apenas_uma_repeticao = []
#lista de retorno
    for caractere in string:
        if caractere not in ocorrencias:
            ocorrencias.append(caractere)
            apenas_uma_repeticao.append(caractere)
        else:
            apenas_uma_repeticao.append('*')
    return ''.join(apenas_uma_repeticao)
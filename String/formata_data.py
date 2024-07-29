def formata_data(data, formato):
    separador = ''
    for caracter in formato:
        if caracter not in 'dma':
            separador = caracter
            break
    partes_data = data.split(separador)
    partes_formato = formato.split(separador)

    dia = partes_data[partes_formato.index('d')] #o dia em data tem o mesmo index que o formato
    mes = partes_data[partes_formato.index('m')]
    ano = partes_data[partes_formato.index('a')]

    if len(ano) == 2:
        ano = '20' + ano
    
    return f'{ano}-{int(mes):02d}-{int(dia):02d}'
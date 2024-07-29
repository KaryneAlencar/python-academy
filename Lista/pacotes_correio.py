def pacotes_correio(lista_remessa):
    total_pacotes = lista_remessa[0][0]
    tamanho_pacote = lista_remessa[0][2]

    if len(lista_remessa) != total_pacotes:
        return 'pacote perdido'
        
    for pacote in lista_remessa:
        if pacote[2] != tamanho_pacote:
            return 'tamanho errado'
    
    for i in range(total_pacotes):
        if lista_remessa[i][1] != i+1:
            return 'ordem errada'

    return 'tudo certo'
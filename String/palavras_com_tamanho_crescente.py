def palavras_com_tamanho_crescente(lista_string):
    for i in range(len(lista_string)-1):
        if len(lista_string[i]) >= len(lista_string[i+1]):
            return False
    return True
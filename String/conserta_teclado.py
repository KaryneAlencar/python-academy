def conserta_teclado(string):
    if not string:
        return ''
    palavra = string.lower()
    corrigida = [palavra[0]]
    for letra in palavra[1:]:
        if letra != corrigida[-1]:
            corrigida.append(letra)
    return ''.join(corrigida)
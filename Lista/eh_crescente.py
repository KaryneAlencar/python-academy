def eh_crescente(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] >= lista[i+1]:
            return False
        i += 1

    return True
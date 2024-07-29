def eh_fibonacci(lista_numeros):
    if len(lista_numeros) < 3:
        return False
    i = 2
    while i < len(lista_numeros):
        if lista_numeros[i] != lista_numeros[i-1] + lista_numeros[i - 2]:
            return False
        i += 1
    return True
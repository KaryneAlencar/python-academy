import math
def quadrados_no_intervalo(a, b):
    quantidade = 0
    i = a
    while i <= b:
        raiz = math.sqrt(i)
        n_int = int(raiz)
        valor = n_int**2
        if valor == i:
            quantidade += 1
        i += 1
    return quantidade
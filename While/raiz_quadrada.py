def raiz_quadrada(n):
    sub = 1
    raiz = 0
    while n > 0:
        n -= sub
        sub += 2
        raiz += 1
    return raiz
print(raiz_quadrada(4))
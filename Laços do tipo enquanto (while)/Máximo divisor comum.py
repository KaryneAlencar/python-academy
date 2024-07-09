def maximo_divisor_comum(n1, n2):
    while n2 != 0:
        resto = n1 % n2
        n1 = n2
        n2 = resto
    return n1
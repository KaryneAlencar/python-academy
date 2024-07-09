def valida_cpf(a, b, c, d, e, f, g, h, i, j, k):
    if a == b and b == c and c == d and d == e and e == f and f == g and g == h and h == i and i == j and j == k:
        return False
    
    operacao1 = ((a*10 + b*9 + c*8 + d*7 + e*6 + f*5 + g*4 + h*3 + i*2)*10) %11
    if operacao1 == 10:
        operacao1 = 0
    
    operacao2 = ((a*11 + b*10 + c*9 + d*8 + e*7 + f*6 + g*5 + h*4 + i*3 + j*2)*10) %11
    if operacao2 == 10:
        operacao2 = 0

    if j == operacao1 and k == operacao2:
        return True
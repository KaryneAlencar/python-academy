def calcula_serie(a, b, n):

    soma = 0
    i = 1
    while i <= (n-1):
        termo = 1/(a**(i*b))
        soma += termo
        i += 1
    resultado = 1 + soma
    return resultado
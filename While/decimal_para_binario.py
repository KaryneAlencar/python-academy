def decimal_para_binario(n):
    if n < 0:
        return 'Negativo'
    binario = ''
    while n > 0:
        resto = n % 2
        binario = str(resto) + binario # nn pode ser += pois a seq dos ninarios é invertida
        n = n // 2
    return binario

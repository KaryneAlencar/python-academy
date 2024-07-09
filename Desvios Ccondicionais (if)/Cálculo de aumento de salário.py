def calcula_aumento(salario):
    if salario > 1250:
        aumento = 0.1 * salario
    else:
        aumento = 0.15 * salario
    return aumento
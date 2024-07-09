import math
def calcula_euler(x, n):
    contador = 0
    soma = 0 
    while contador < n:
        termo = (x**contador)/math.factorial(contador)
        soma += termo
        contador +=1
    return soma
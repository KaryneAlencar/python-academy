import math
def calcula_norma(vetor):
    soma = 0
    i = 0
    while i < len(vetor):
        soma += vetor[i]**2
        i += 1
    norma = math.sqrt(soma)
    return norma
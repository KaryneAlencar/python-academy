import math
def calcula_pi(n):
    denominador = 1
    resposta = 0
    while denominador <= n:
        pi = 6/(denominador**2)
        resposta += pi
        denominador += 1
    resposta_final = math.sqrt(resposta)
    return resposta_final
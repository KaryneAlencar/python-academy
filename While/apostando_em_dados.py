import random
def apostando_em_dados(n, v, r):
    rodada = 1
    acumulativo = v
    while rodada <= r:
        sorteado = random.randint(1,6)
        if n == sorteado:
            acumulativo += (1/3)*acumulativo
        else:
            acumulativo -= (1/6)*acumulativo
        rodada += 1
    
    return acumulativo
import random
def distribuir(n, lista_possivel):
    lista_bingo = []
    while len(lista_bingo) < n:
        numero_sorteado = random.choice(lista_possivel)
        if numero_sorteado not in lista_bingo:
            lista_bingo.append(numero_sorteado)
    return lista_bingo
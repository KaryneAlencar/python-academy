def lista_caracteres(string):
    sem_repeticao = []
    for letra in string:
        if letra not in sem_repeticao:
            sem_repeticao.append(letra)
    return sem_repeticao
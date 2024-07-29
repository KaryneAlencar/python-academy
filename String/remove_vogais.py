def remove_vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']
    sem_vogais = ''
    for letra in string:
        if letra not in vogais:
            sem_vogais += letra
    return sem_vogais
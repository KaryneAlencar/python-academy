def remove_vogais(string):
    vogais = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    sem_vogal = ''
    for letra in string:
        if letra not in vogais:
            sem_vogal += letra
    return sem_vogal
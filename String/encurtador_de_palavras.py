vogais = ['a', 'e', 'i', 'o', 'u']
while True:
    palavra = input('Digite uma palavra: ')

    if palavra == 'fim':
        break
    palavra_sem_vogal = ''
    for letra in palavra:
        if letra not in vogais:
            palavra_sem_vogal += letra
    print(palavra_sem_vogal)
print('Até a próxima')
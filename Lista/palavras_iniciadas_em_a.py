lista_palavras = []
verifica = True
while verifica:
    palavra = input('Digite uma palavra: ')
    if palavra == 'fim':
        verifica = False
    else:
        lista_palavras.append(palavra)

for palavra in lista_palavras:
    if palavra[0] == 'a':
        print(palavra)

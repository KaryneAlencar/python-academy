lista = []
verifica = True
while verifica:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero <= 0:
        verifica = False

lista_inversa = []
i = len(lista)-1
while i >= 0:
    lista_inversa.append(lista[i])
    i -=1
#lista_invesa = lista[::-1]
print(lista_inversa)
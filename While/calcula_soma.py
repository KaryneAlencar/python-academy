zero = True
contador = 0
while zero:
    n = int(input('Digite um número: '))
    contador += n
    if n == 0:
        zero = False
print(contador)
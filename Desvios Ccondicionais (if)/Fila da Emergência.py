cor = input('Classificação? (V/L/A)')
v = int(input('Quantos Vermelhos estão aguardando?'))
l = int(input('Quantos Laranjas estão aguardando?'))
a = int(input('Quantos Azuis estão aguardando?'))

if cor == 'V':
    tempo = v * 7
elif cor == 'L':
    tempo = v * 7 + l * 5
else:
    tempo = v * 7 + l * 5 + a * 5

print(tempo)
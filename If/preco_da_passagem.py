distancia = int(input('Qual a distância a ser percorrida em Km?'))

if distancia <= 200:
    preco = 0.50*distancia
else:
    extra = distancia - 200
    preco = (0.50 * 200) + (0.45 * extra)

print(f'{preco:.2f}')
dias = int(input('Qual a quantidade de dias para análise?'))

dia = 1
soma_precos = 0
melhor_dia = 0
menor_preco = float('inf')
pior_dia = 0
pior_preco = 0
while dia <= dias:
    preco = float(input('Preco do dísel em cada dia: '))
    soma_precos += preco
    if menor_preco > preco:
        menor_preco = preco
        melhor_dia = dia
    if pior_preco < preco:
        pior_preco = preco
        pior_dia = dia
    dia += 1

media = soma_precos/dias
print(f'O dia {melhor_dia} foi o melhor dia para compra')
print(f'O dia {pior_dia} foi o pior dia para compra')
print(f'O preço médio cobrado foi de {media:.2f}')
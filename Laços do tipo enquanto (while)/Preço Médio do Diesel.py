dias = int(input('Qual a quantidade de dias para análise?'))

dia = 0
soma_precos = 0
while dia < dias:
    preco = float(input('Preco do dísel em cada dia: '))
    soma_precos += preco
    dia += 1

media = soma_precos/dias
print(f'O preço médio cobrado foi de {media:.2f}')
tamanho = input('Tamanho [P/M/G]')
borda = input('Borda recheada [S/N]?')
queijo = input('Adicional de queijo [S/N]?')
refrigerante = input('Refrigerante [S/N]?')
sobremesa = input('Sobremesa [S/N]?')

#refrigerante
if refrigerante == 'S':
    conta_r = 12
if refrigerante == 'N':
    conta_r = 0

#tamanho
if tamanho == 'P':
    conta_t = 50
elif tamanho == 'M':
    conta_t = 70
elif tamanho == 'G':
    conta_t = 90

#borda 
if borda == 'S':
    conta_b = 0.15 * conta_t
if borda == 'N':
    conta_b = 0

#queijo 
if queijo == 'S':
    conta_q = 0.1 * conta_t
if queijo == 'N':
    conta_q = 0

#sobremesa
if sobremesa == 'S' and tamanho == 'G':
    preco_s = 20
    desconto = (preco_s + conta_q + conta_b + conta_r + conta_t)*0.07
    total2 = (preco_s + conta_q + conta_b + conta_r + conta_t) - desconto
    print(f'{total2:.2f}')
if sobremesa == 'S':
    preco_s = 20
if sobremesa == 'N':
    preco_s = 0

total = conta_r + conta_t + conta_b + conta_q + preco_s
print(f'{total:.2f}')
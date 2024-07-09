r2 = float(input('Qual o valor do R2?'))
n = int(input('Qual o valor do n?'))
p = int(input('Qual o valor do p?'))

r2_ajus = 1 - ((1-r2)*(n-1)/(n - p - 1))

print(f'{r2_ajus:.4f}')
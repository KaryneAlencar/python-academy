import math
taxa = float(input('Qual a taxa (λ)?'))
x = float(input('Qual x, para calcular F(λ, x)?'))

F = 1 - math.e**(-taxa*x)
print(f'{F:.4f}')
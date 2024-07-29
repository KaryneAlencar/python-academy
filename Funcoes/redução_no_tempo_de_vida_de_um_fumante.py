cigarros = int(input('Quantos cigarros você fuma por dia?'))
anos = int(input('Há quantos anos você fuma?'))

dias_fumados = anos * 365
total_cigarros = dias_fumados * cigarros
temp_perdido_min = total_cigarros * 10
temp_perdido_dias = temp_perdido_min / (24*60)

print('O tempo de vida perdido foi de', temp_perdido_dias, 'dias')
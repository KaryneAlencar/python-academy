dias = int(input('Quantos dias você quer analisar?'))

dias_chuva = 0
dias_frio = 0
dias_gc = 0
dias_c = 0

i = 1
while i <= dias:
    chuva = input('Choveu [S/N]?')
    t_min = int(input('Temperatura mínima (em Celsius)?'))
    gc = input('Tinha guarda-chuva [S/N]')
    c = input('Tinha casaco [S/N]?')

    if chuva == 'S':
        dias_chuva += 1
        if gc == 'S':
            dias_gc += 1
    if t_min < 20:
        dias_frio += 1
        if c == 'S':
            dias_c += 1
    i += 1

print(f'Choveu em {dias_chuva} de {dias} dias')
print(f'Fez frio em {dias_frio} de {dias} dias')
print(f'Usou guarda-chuva em {dias_gc} de {dias_chuva} dias de chuva')
print(f'Usou casaco em {dias_c} de {dias_frio} dias de frio')
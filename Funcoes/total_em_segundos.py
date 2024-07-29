dias = int(input('Qual a quantidade de dias?'))
horas = int(input('Qual a quantidade de horas?'))
minutos = int(input('Qual a quantidade de minutos?'))
segundos = int(input('Qual a quantidade de segundos?'))

min_seg = minutos*60
h_seg = (horas*60)*60
d_seg = ((dias*24)*60)*60

total_seg = segundos + min_seg + h_seg + d_seg
print(f'O total de segundos é {total_seg}')
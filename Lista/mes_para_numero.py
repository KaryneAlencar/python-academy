mes = input('Digite o nome do mês: ')

lista_mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
lista_mes_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

i = 0
while i < len(lista_mes):
    if lista_mes[i] == mes:
        print(lista_mes_num[i])
        break
    i += 1
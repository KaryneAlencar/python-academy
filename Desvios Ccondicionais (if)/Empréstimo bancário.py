casa = float(input('Qual o valor da casa a ser comprada?'))
salario = float(input('Qual o valor do salário?'))
anos = int(input('Qual a quantidade de anos a pagar?'))

if casa/(anos*12) < 0.3*salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')
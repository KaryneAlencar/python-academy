velocidade = float(input('Qual a velocidade?'))
if velocidade > 80:
    excesso = velocidade - 80
    multa = 5 * excesso
    print(f'A multa é de R$ {multa:.2f}')
else:
    print('Não foi multado')
verifica = True
while verifica:
    entrada = input('Digite algo: ')
    if entrada == 'oi':
        print('Olá!')
    elif entrada == 'bom dia':
        print('Bom dia')
    elif entrada == 'site':
        print('Acesse https://insper.edu.br')
    elif entrada == 'blackboard':
        print('Lá temos materiais, notas e muito mais!')
    elif entrada == 'tchau' or entrada == 'encerrar':
        print('Até logo')
        verifica = False
    else:
        print('Não sei como te ajudar!')
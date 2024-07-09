plano = input('Qual é o seu plano? ')
valida = True
while valida:
    serie = input('Qual série deseja assistir? ')
    if serie == 'stranger things':
        if plano == 'novo':
           print('Precisa comprar novo plano!') 
        elif plano == 'padrao':
            print('Ok, reproduzindo!')
        else:
            print('Ok, reproduzindo!')
    
    elif serie == 'friends':
        if plano == 'novo':
           print('Precisa comprar novo plano!') 
        elif plano == 'padrao':
            print('Ok, reproduzindo!')
        else:
            print('Ok, reproduzindo!')
    
    elif serie == 'the circle':
        if plano == 'novo':
           print('Ok, reproduzindo!') 
           print('Num oferecimento de DesSoft!')
        elif plano == 'padrao':
            print('Ok, reproduzindo!')
        else:
            print('Ok, reproduzindo!')

    elif serie == 'mad men':
        if plano == 'novo':
           print('Ok, reproduzindo!') 
           print('Num oferecimento de DesSoft!')
        elif plano == 'padrao':
            print('Ok, reproduzindo!')
        else:
            print('Ok, reproduzindo!')
    
    elif serie == 'brasileirao':
        if plano == 'novo':
           print('Precisa comprar novo plano!') 
        elif plano == 'padrao':
            print('Precisa comprar novo plano!')
        else:
            print('Ok, reproduzindo!')

    elif serie == 'champions':
        if plano == 'novo':
           print('Precisa comprar novo plano!') 
        elif plano == 'padrao':
            print('Precisa comprar novo plano!')
        else:
            print('Ok, reproduzindo!')
    
    elif serie == 'sair':
        print('Ok, tchau!')
        valida = False
    
    else:
        print('Serie inexistente!')
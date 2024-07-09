def pedra_papel_tesoura(j1, j2):
    if j1 == 'pedra' and j2 == 'pedra':
        return 'empate'
    elif j1 == 'papel' and j2 == 'papel':
        return 'empate'
    elif j1 == 'tesoura' and j2 == 'tesoura':
        return 'empate'
    
    elif j1 == 'pedra' and j2 == 'papel':
        return 'dois'
    elif j1 == 'pedra' and j2 == 'tesoura':
        return 'um'
    elif j1 == 'papel' and j2 == 'tesoura':
        return 'dois'
    elif j1 == 'papel' and j2 == 'pedra':
        return 'um'
    elif j1 == 'tesoura' and j2 == 'pedra':
        return 'dois'
    elif j1 == 'tesoura' and j2 == 'papel':
        return 'um'
    
    else:
        return 'Escolha pedra, papel ou tesoura para jogar'
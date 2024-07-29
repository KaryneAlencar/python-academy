def verifica_jogo_da_velha(tabuleiro):
    #verifica na horizontal
    for linha in tabuleiro:
        #verifica na horizontal
        if linha[0] == linha[1] and linha[1] == linha[2]:
            return linha[0] #retorna a string da linha 
       
    #verifica na vertical
    if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:
        return tabuleiro[0][0]
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:
        return tabuleiro[0][1]
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:
        return tabuleiro[0][2]
    
    #verifica diagonal
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return tabuleiro[0][2]
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return tabuleiro[0][0]
    else:
        return 'V'
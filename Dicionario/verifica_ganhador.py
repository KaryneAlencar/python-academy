def verifica_ganhador(dic_domino):
    for jogador, pecas in dic_domino.items():
            if pecas == []:
                  return jogador
    return -1       

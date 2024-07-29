def define_vencedores(lista_bingo, dic_jogadores):
    pontos = {}
    for jogador, marcacao in dic_jogadores.items():
        for numero in marcacao:
            if numero in lista_bingo:
                if jogador in pontos:
                    pontos[jogador] += 1
                else:
                    pontos[jogador] = 1
            else:
                pontos[jogador] = 0
    
    maior_ponto = -1
    for ponto in pontos.values():
        if ponto > maior_ponto:
            maior_ponto = ponto
    if maior_ponto == -1:
        maior_ponto = 0
    
    vencedores = []
    for jogador, ponto in pontos.items():
        if ponto == maior_ponto:
            vencedores.append(jogador)
    
    return vencedores


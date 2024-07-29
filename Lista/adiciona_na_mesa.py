def adiciona_na_mesa(peca, mesa):
    if len(mesa) == 0:
        mesa.append(peca)

    esquerda_mesa = mesa[0][0]
    direita_mesa = mesa[-1][1]

    # Verificando se a peça pode ser encaixada na esquerda
    if peca[1] == esquerda_mesa:
        return [peca] + mesa
    elif peca[0] == esquerda_mesa:
        return [peca[::-1]] + mesa
    
    # Verificando se a peça pode ser encaixada na direita
    if peca[0] == direita_mesa:
        return mesa + [peca]
    elif peca[1] == direita_mesa:
        return mesa + [peca[::-1]]
    
    # Caso não possa ser encaixada, retornamos a mesa inalterada
    return mesa
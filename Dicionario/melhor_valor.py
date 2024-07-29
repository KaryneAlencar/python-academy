def melhor_valor(pecas_trocar, lista_estoque):
    soma = 0
    for peca in pecas_trocar:
        melhor_valor = float('inf')
        for estoque in lista_estoque:
            if estoque['serial'] == peca or peca in estoque['equivalente']:
                if estoque['valor'] < melhor_valor:
                    melhor_valor = estoque['valor']

        if melhor_valor == float('inf'):
            melhor_valor = 0
        soma += melhor_valor
        
    return soma
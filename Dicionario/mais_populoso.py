def mais_populoso(brasil):
    estado_pop = ''
    populacao = 0
    for estado, info in brasil.items():
        pop_estado = 0
        for valores in info.values():
            pop_estado += valores
        if pop_estado > populacao:
            populacao = pop_estado
            estado_pop = estado
    return estado_pop
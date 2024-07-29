def classifica(categorias, peixe):
    menor_distancia = float('inf')
    categoria_mais_proxima = ''
    
    for categoria, padroes in categorias.items():
        for padrao in padroes:
            distancia = (peixe[0] - padrao[0]) ** 2 + (peixe[1] - padrao[1]) ** 2
            if distancia < menor_distancia:
                menor_distancia = distancia
                categoria_mais_proxima = categoria
                
    return categoria_mais_proxima
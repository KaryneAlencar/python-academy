import math
def caminho_mais_curto(lista_caminhos):
    menor_caminho = float('inf')
    caminho_mais_curto = []
    for caminho in lista_caminhos:
        distancia = 0
        for i in range(len(caminho)-1):
            distancia += math.sqrt((caminho[i+1][0] - caminho[i][0])**2 + (caminho[i+1][1] - caminho[i][1])**2)
        if distancia < menor_caminho:
            menor_caminho = distancia
            caminho_mais_curto = caminho
    return caminho_mais_curto
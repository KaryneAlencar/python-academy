import math
def entregador_mais_proximo(restaurante, lista_estregadores):
    menor_dist = float('inf')
    indice = -1
    i = 0
    while i < len(lista_estregadores):
        for entregador in lista_estregadores:
            dist = math.sqrt((entregador[0]-restaurante[0])**2 + (entregador[1]-restaurante[1])**2)
            if dist < menor_dist:
                menor_dist = dist
                indice = i
            i += 1
    return indice

#usando for ------------------------------
import math
def entregador_mais_proximo(restaurante, lista_estregadores):
    menor_dist = float('inf')
    indice = -1
    for i in range(len(lista_estregadores)):
        entregador = lista_estregadores[i]
        dist = math.sqrt((entregador[0]-restaurante[0])**2 + (entregador[1]-restaurante[1])**2)
        if dist < menor_dist:
            menor_dist = dist
            indice = i
    return indice
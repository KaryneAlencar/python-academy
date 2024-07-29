import math
def calcula_extensao(listax, listay):
    extensao = 0
    for i in range(len(listax)-1):
        deltax = listax[i+1] - listax[i]
        deltay = listay[i+1] - listay[i]
        
        dist = math.sqrt(deltax**2 + deltay**2)
        extensao += dist

    return extensao
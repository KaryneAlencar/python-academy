import math
def calcula_distancia_do_projetil(v, a,yi):
    g = 9.8
    raiz = math.sqrt(1+(2*g*yi)/(v**2*(math.sin(a)**2)))
    d = ((v**2)/(2*g)) * (1 + raiz) * math.sin((2*a))
    return d
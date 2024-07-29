import math
def haversine(raio, fi1, gama1, fi2, gama2):
    #transforma os ângulos para radianos
    fi1 = math.radians(fi1)
    gama1 = math.radians(gama1)
    fi2 = math.radians(fi2)
    gama2 = math.radians(gama2)

    latitude = (fi2 - fi1)/2
    longitude = (gama2 - gama1)/2

    d = 2 * raio * math.asin(math.sqrt(math.sin(latitude)**2 + math.cos(fi1) * math.cos(fi2) * math.sin(longitude)**2))
    return d
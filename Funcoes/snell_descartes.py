import math
def snell_descartes(n1, n2, teta1):
    teta1 = math.radians(teta1)
    teta2 = math.degrees(math.asin((math.sin(teta1)*n1)/n2))
    return teta2
import math
def area_pentagono(l):
    apotema = l/(2*math.tan(math.pi/5))
    area = (5 * l * apotema)/2
    return area
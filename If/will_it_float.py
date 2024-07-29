import math
def will_it_float(p, R, r):
    volume = 2 * math.pi**2 * R * r**2
    peso = p * 1000
    densidade = peso/volume

    if densidade <= 0.997:
        return True
    else:
        return False
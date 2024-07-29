import math
def reflexao_total_interna(n1, n2, teta2):
    teta2 = math.radians(teta2)
    sin_teta1 = (math.sin(teta2) * n2)/n1
    if sin_teta1 > 1:
        return True
    else:
        return False
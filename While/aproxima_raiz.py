def aproxima_raiz(n):
    i = 1
    maior = 0
    while i**2 <= n:
        if i > maior:
            maior = i
        i += 1

    if abs(((i-1)**2) - n) > abs(i**2 - n):
        return i
    else:
        return i-1    

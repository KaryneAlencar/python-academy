def analisa_investimento(i, f, m):
    if i <= 0 or f <= 0 or m <= 0:
        return 0
    
    j = ((f/i)**(1/m))-1

    if j > 0.01:
        return 3
    elif j >= 0.003 and j <= 0.01:
        return 2
    else:
        return 1
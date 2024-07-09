def PiWallis(n):
    produto = 1
    fator = 2
    i = 1  

    while i <= n:
        if i % 2 == 0:
            produto *= fator / (fator + 1)
            fator += 2
        else: 
            produto *= fator / (fator - 1)
        i += 1 
    pi = 2 * produto
    return pi

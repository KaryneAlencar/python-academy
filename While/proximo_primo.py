def proximo_primo(n):
    prox = n + 1
    while True:
        if prox <= 1:
            prox += 1
        if prox <= 3:
            return prox
        if prox % 2 == 0 or prox % 3 == 0:
            prox += 1
            
    i = 5
    verifica = True
    while i * i <= prox:
        if prox % i == 0:
            verifica = False
        i += 2
    return prox
            



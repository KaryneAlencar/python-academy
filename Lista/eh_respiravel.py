def eh_respiravel(matriz_fotografia):
    oxigenio = 0
    total = 0
    for linha in matriz_fotografia:
        for elemento in linha:
            total += 1
            if elemento == 'O':
                oxigenio += 1
    if 0.2 * total <= oxigenio:
        return True
    else:
        return False
                


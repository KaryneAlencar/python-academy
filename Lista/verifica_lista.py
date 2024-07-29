def verifica_lista(lista):
    par = False
    impar = False
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0: #verifica se tem par e impar
            par = True
        else:
            impar = True
        i += 1
    if par and impar: #se par e impar forem True
        return 'misturado'
    elif par:
        return 'par'
    elif impar:
        return 'ímpar'
    else:
        return 'misturado'
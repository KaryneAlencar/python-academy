def lista_celulares(numeros):
    celulares = []

    for numero in numeros:
        if len(numero) >= 3 and numero[:3] == '+55':
            numero = numero[3:]

        if len(numero) in [10, 11] and numero[2] == '9':
            celulares.append(numero[2:])

        elif len(numero) in [8, 9] and numero[0] == '9':
            celulares.append(numero)

    return celulares



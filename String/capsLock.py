def capsLock(string):
    formatado = []
    for letra in string:
        if letra.islower():
            formatado.append(letra.upper())
        elif letra.isupper():
            formatado.append(letra.lower())
        else:
            formatado.append(letra)
    return ''.join(formatado)
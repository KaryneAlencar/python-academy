def fatorial(n):
    contador = 1
    resultado = 1
    while contador <= n:
        resultado *= contador 
        contador += 1
    return resultado

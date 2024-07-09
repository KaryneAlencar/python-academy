def soma_multiplos(n1,n2):
    maior = n1
    if n2 > maior:
        maior = n2

    limite = maior * 10

    i = 0
    soma = 0
    while i <= limite:
        if i % n1 == 0 or i % n2 == 0: # se o número é multiplo de algum dos termos
            soma += i
        i += 1
    return soma

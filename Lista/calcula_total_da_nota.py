def calcula_total_da_nota(lista1, lista2):
    conta = []
    i = 0
    while i < len(lista1):
        conta += lista1[i]*lista2[i]
        i += 1
    return conta
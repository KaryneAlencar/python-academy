def produz_um_dois_insper(numero_inicial, numero_final, multiplo):
    lista_isper = []
    for i in range(numero_inicial, numero_final+1):
        if i % multiplo == 0:
            lista_isper.append('Insper')
        else:
            lista_isper.append(i)
    return lista_isper
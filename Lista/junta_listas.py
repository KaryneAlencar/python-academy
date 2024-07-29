def junta_listas(listas):
    lista_planarizada = []
    for lista in listas:
            lista_planarizada += lista #soma de listas
    return lista_planarizada
#----------------------------------
def junta_listas(listas):
    lista_planarizada = []
    for lista in listas:
        for elemento in lista:
            lista_planarizada.append(elemento)
    return lista_planarizada
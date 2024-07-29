def valida_data(d, m, a):
    #confere os meses
    if m > 12 or m == 0:
        return False   
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d > 31 or d == 0:
            return False
        else:
            return True
    if m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30 or d == 0:
            return False
        else:
            return True
        
    #confere ano bissexto 
    if a % 4 == 0 and a % 400 == 0:
        if m == 2:
            return not(d > 29 or d == 0) #se a condição do parêntese é verdadeira, retorna o oposto e visse versa
            #if d > 29 or d == 0:
            #    return False
            #else:
            #    return True
    else:
        if m == 2:
            return not(d > 28 or d == 0) 
def verifica_progressao(lista_n):
  
    arit = True
    geo = True
    razao_pa = lista_n[1] - lista_n[0]
    razao_pg = lista_n[1] / lista_n[0] if lista_n[0] != 0 else None
    
    for i in range(1, len(lista_n)):
        # Verificação da PA
        if lista_n[i] - lista_n[i-1] != razao_pa:
            arit = False
        # Verificação da PG
        if lista_n[i-1] == 0 or lista_n[i] / lista_n[i-1] != razao_pg:
            geo = False
    
    if arit and geo:
        return 'AG'
    elif arit:
        return 'PA'
    elif geo:
        return 'PG'
    else:
        return 'NA'

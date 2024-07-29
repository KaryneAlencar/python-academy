def compras_da_semana(dic_receitas, lista_pratos):
    dic_ingredientes = {}
    
    for prato in lista_pratos:
        if prato in dic_receitas:
            for ingrediente, quantidade in dic_receitas[prato].items():
                if ingrediente in dic_ingredientes:
                    dic_ingredientes[ingrediente] += quantidade
                else:
                    dic_ingredientes[ingrediente] = quantidade 
    
    return dic_ingredientes


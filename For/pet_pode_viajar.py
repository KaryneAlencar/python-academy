def pet_pode_viajar(lista_pet, lista_limite, lista_passagem):
    #lista sobre o pet
    nome = lista_pet[0]
    especie = lista_pet[1]
    peso_pet = lista_pet[2]
    peso_caixa = lista_pet[3]
    dimensao = lista_pet[4]
    atestado = lista_pet[5]

    #informações da caixa
    altura = dimensao[0]
    largura = dimensao[1]
    profundidade = dimensao[2]

    #lista sobre os limites do voo
    limite_pets = lista_limite[0]
    limite_peso = lista_limite[1]
    limite_dimensao = lista_limite[2]

    #limites da caixa
    limite_altura = limite_dimensao[0]
    limite_largura = limite_dimensao[1]
    limite_profundidade = limite_dimensao[2]

    if atestado != 'S':
        return False
    
    peso_total = peso_pet + peso_caixa
    if peso_total > limite_peso:
        return False
    
    if altura > limite_altura or largura > limite_largura or profundidade > limite_profundidade:
        return False
    
    pets_na_cabine = 0
    for assento in lista_passagem:  # Itera sobre cada assento em lista_passagem
        solicitacoes = assento[1]  # Acessa a lista de solicitações desse assento
        if 'pet_cabine' in solicitacoes:  # Verifica se 'pet_cabine' está na lista de solicitações
            pets_na_cabine += 1
    if pets_na_cabine >= limite_pets:
        return False
    
    return True

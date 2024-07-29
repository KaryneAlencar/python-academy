def mais_medalhas(lista_atletas):
    mais_ouro = 0
    nac = ''
    for dic in lista_atletas:
         if dic['ouro'] > mais_ouro:
            mais_ouro = dic['ouro']
            nac = dic['nacionalidade']
    return nac

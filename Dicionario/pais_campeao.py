def pais_campeao(medalhas):
    campeao = ''
    maior_ouro = -1
    for pais,medalha in medalhas.items():
        if medalha['ouro'] > maior_ouro:
            campeao = pais
            maior_ouro = medalha['ouro']
        elif medalha['ouro'] == maior_ouro:
            if medalha['prata'] > medalhas[campeao]['prata']:
                campeao = pais
            elif medalha['prata'] == medalhas[campeao]['prata']:
                if medalha['bronze'] > medalhas[campeao]['bronze']:
                    campeao = pais
    return campeao
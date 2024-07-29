def calcula_tempo(dic_atletas):
    tempo = {}
    for atleta, aceleracao in dic_atletas.items():
        tempo[atleta] = (200/aceleracao)**0.5
    return tempo

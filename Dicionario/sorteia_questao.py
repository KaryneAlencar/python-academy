#recebe o dicionario de questoes e o nivel desejado e sortei uma delas
import random
def sorteia_questao(dic_questoes_nivel, nivel):
    if nivel in dic_questoes_nivel:
        q_sorteada = random.choice(dic_questoes_nivel[nivel])
        return q_sorteada
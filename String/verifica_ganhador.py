def verifica_ganhador(texto, dic_bingo):
    dic_pontos = {}
    minusculo_texto = texto.lower()
    lista_texto = minusculo_texto.split()
    
    for nome, respostas in dic_bingo.items():
        pontos = 0
        for resposta in respostas:
            resposta_lower = resposta.lower()
            for palavra in lista_texto:
                if palavra == resposta_lower:
                    pontos += 1
        dic_pontos[nome] = pontos
    return dic_pontos
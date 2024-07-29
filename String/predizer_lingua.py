def predizer_lingua(dic_lingua, string):
    caracteres_indevidos = ['!', '?', ',', ';', '.', ':', ')', '}', ']', '(', '[', '{']
    texto_limpo = ''
    for letra in string:
        if letra not in caracteres_indevidos:
            texto_limpo += letra
    texto_minusculo = texto_limpo.lower()
    lista_texto = texto_minusculo.split()

    total_palavras = len(lista_texto)
    if total_palavras == 0:
        dic_palpite = {lingua: 0.0 for lingua in dic_lingua}
        dic_palpite['palpite'] = 'DESCONHECIDA'
        return dic_palpite
    
    dic_palpite = {}
    for lingua, palavras in dic_lingua.items():
        contagem_palavra = 0
        for palavra in lista_texto:
            if palavra in palavras:
                contagem_palavra += 1
        dic_palpite[lingua] = contagem_palavra / total_palavras
    
    maior_numero = 0.0
    lingua_palpite = ''
    for lingua, contagem in dic_palpite.items():
        if contagem > maior_numero:
            maior_numero = contagem
            lingua_palpite = lingua
        elif contagem == maior_numero:
            lingua_palpite = 'DESCONHECIDA'
    
    dic_palpite['palpite'] = lingua_palpite
    return dic_palpite
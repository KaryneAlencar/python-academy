import re
def conta_palavras(texto):
    contagem = {}
    texto_limpo = re.sub(r'[?!.,]', '', texto.lower())
    palavras = texto_limpo.split()

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

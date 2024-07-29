def tamanho_minimo(texto ,n):
    senhas = []
    palavras = texto.split()
    for palavra in palavras:
        if len(palavra) > n:
            senhas.append(palavra)
    return senhas
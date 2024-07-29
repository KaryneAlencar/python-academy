def esconde_senha(string):
    senha = ''
    for letra in string:
        senha += '*'
    return senha
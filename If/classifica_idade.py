def classifica_idade(idade):
    if idade <= 11:
        string = 'crianca'
    elif 12 <= idade <= 17:
        string = 'adolescente'
    else:
        string = 'adulto'
    return string

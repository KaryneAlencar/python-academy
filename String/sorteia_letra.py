import random

def sorteia_letra(palavra, restricao):
    palavra = palavra.replace(" ", "").lower()
    restricoes = []
    for elemento in restricao:
        restricoes.append(elemento.lower())
        
    carac_especial = ['.', ',', '-', ';', ' ']

    carac_validos = []
    for letra in palavra:
        if letra not in restricoes and letra not in carac_especial:
            carac_validos.append(letra)
    
    if carac_validos == []:
        return ''
        
    sorteado = random.choice(carac_validos)
    return sorteado
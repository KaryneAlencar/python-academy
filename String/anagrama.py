def anagrama(string1, string2):
    if len(string1) != len(string2):
        return False

    contagem1 = {}
    contagem2 = {}

    for letra in string1:
        if letra not in contagem1:
            contagem1[letra] = 1
        else:
            contagem1[letra] += 1
    
    for letra in string2:
        if letra not in contagem2:
            contagem2[letra] = 1
        else:
            contagem2[letra] += 1

    for letra, contagem in contagem1.items():
        if letra not in contagem2:
            return False
        if letra in contagem2 and contagem != contagem2[letra]:
            return False
    return True
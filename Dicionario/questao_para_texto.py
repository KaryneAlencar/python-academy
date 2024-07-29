#recebe um dicionario em forma de questao e um id representando o numero da questao e retorna a questao formatada
def questao_para_texto(questao, id):
    # Extraindo as informações do dicionário de entrada
    titulo = questao["titulo"]
    opcoes = questao["opcoes"]
    
    # Construindo a string formatada
    resultado = f"----------------------------------------\n"
    resultado += f"QUESTAO {id}\n\n"
    resultado += f"{titulo}\n\n"
    resultado += "RESPOSTAS:\n"
    
    for opcao, descricao in opcoes.items():
        resultado += f"{opcao}: {descricao}\n"
    
    return resultado


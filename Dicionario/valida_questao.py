#recebe uma questão em forma de decionario e retona se ela tem erros
def valida_questao(questao): 
    valida = {}

    # Verifica se todas as chaves necessárias estão na questão
    chaves = ['titulo', 'nivel', 'opcoes', 'correta']
    for chave in chaves:
        if chave not in questao:
            valida[chave] = 'nao_encontrado'
    
    # Verifica se a questão possui exatamente 4 chaves
    if len(questao) != 4:
        valida['outro'] = 'numero_chaves_invalido'

    # Verifica se o título está vazio ou contém apenas espaços
    if 'titulo' in questao and not questao['titulo'].strip():
        valida['titulo'] = 'vazio'

    # Verifica se o nível é 'facil', 'medio' ou 'dificil'
    if 'nivel' in questao and questao['nivel'] not in ['facil', 'medio', 'dificil']:
        valida['nivel'] = 'valor_errado'
    
    # Verifica se a chave 'opcoes' existe e tem 4 opções e se essas sao validas ou estao vazias
    opcoes_validas = ['A', 'B', 'C', 'D']
    if 'opcoes' in questao:
        if len(questao['opcoes']) != 4:
            valida['opcoes'] = 'tamanho_invalido'
        else:
            for opcao in questao['opcoes']:
                if opcao not in opcoes_validas:
                    valida['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    break
                if not questao['opcoes'][opcao].strip():
                    if 'opcoes' not in valida:
                        valida['opcoes'] = {}
                    valida['opcoes'][opcao] = 'vazia'

    # Verifica se existe a chave 'correta'
    if 'correta' not in questao:
        valida['correta'] = 'nao_encontrado'
    elif questao['correta'] not in opcoes_validas:
        valida['correta'] = 'valor_errado'

    return valida
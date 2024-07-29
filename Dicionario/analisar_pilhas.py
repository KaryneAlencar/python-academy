def analisar_pilhas(modelos, pilhas):
    resultados = []
    
    for marca, modelo, voltagem_medida in pilhas:
        # Verificar se a marca e modelo existem no dicionário de modelos
        if marca not in modelos or modelo not in modelos[marca]:
            resultados.append('E')
            continue
        
        modelo_info = modelos[marca][modelo]
        voltagem_nominal = modelo_info['volts']
        limite = modelo_info['limite']
        recarregavel = modelo_info['recarregavel']
        
        # Calcular o limite permitido
        limite_inferior = voltagem_nominal * (1 - limite)
        
        # Analisar o status da pilha
        if voltagem_medida >= limite_inferior:
            resultados.append('N')
        elif recarregavel:
            resultados.append('R')
        else:
            resultados.append('D')
    
    return resultados
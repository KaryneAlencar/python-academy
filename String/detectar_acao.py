def detectar_acao(dic_mensagem, lista_stop_words):
    sufixos_verbais = ['ar', 'er', 'ir', 'or']
    dic_acoes = {}

    for nome, items in dic_mensagem.items():
        acoes_usuario = []
        for msg in items.values():
            palavras = msg.split()
            for i in range(len(palavras)):
                palavra = palavras[i]
                # Verificando se a palavra termina com qualquer um dos sufixos verbais
                is_verbo = False
                for sufixo in sufixos_verbais:
                    if palavra[-len(sufixo):] == sufixo:
                        is_verbo = True
                        break
                # Se for verbo e não estiver na lista de stop-words
                if is_verbo and palavra not in lista_stop_words:
                    if i + 1 < len(palavras) and palavras[i + 1] not in lista_stop_words:
                        acoes_usuario.append(f"{palavra} {palavras[i + 1]}")
                    else:
                        acoes_usuario.append(palavra)
                    break
        dic_acoes[nome] = acoes_usuario
    return dic_acoes
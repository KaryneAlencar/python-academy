def verifica_preco(titulo, dic_nome_cor, dic_cor_preco):
    cor_associada = dic_nome_cor[titulo]
    preco = dic_cor_preco[cor_associada]
    return preco

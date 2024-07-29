def valor_a_devolver(preco_prateleira, preco_caixa, lista_compras):
    valor_devolvido = 0
    for compra in lista_compras:
        produto = compra[0]
        marca = compra[1]
        quantidade = compra[2]
        prateleira = preco_prateleira[produto][marca]
        caixa = preco_caixa[produto][marca]

        if prateleira < caixa:
            tem_que_devolver = abs(prateleira-caixa)*quantidade
            valor_devolvido += tem_que_devolver
    return valor_devolvido
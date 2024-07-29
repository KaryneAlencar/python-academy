def contabiliza(doacoes):
    resultado = {}
    
    for itens in doacoes.values():
        for item in itens:
            quantidade, descricao = item.split(' ', 1)
            quantidade = int(quantidade)
            
            if descricao in resultado:
                resultado[descricao] += quantidade
            else:
                resultado[descricao] = quantidade
    
    return resultado


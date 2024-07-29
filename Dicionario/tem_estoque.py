def tem_estoque(dic_const, dic_estoque):
    for peca, quantidade in dic_const.items():
        if peca not in dic_estoque:
            return False
        if dic_estoque[peca] < quantidade:
            return False
    return True
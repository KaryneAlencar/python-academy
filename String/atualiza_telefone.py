def atualiza_telefone(telefone):
    telefone_atualizado = '9'
    if '-' in telefone:
        if len(telefone)==10:
            return telefone
        else:
            return telefone_atualizado + telefone
    if len(telefone) == 9:
        return telefone
    if len(telefone) == 8:
        return telefone_atualizado + telefone
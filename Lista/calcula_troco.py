def calcula_troco(valor_compra, valor_pago, lista_notas):
    troco = []
    valor_troco = valor_pago - valor_compra

    for nota in lista_notas:
        qnt = valor_troco//nota
        if qnt >0:
            if nota >= 1:
                troco.append(troco.append(f'{qnt} nota(s) de R$ {nota:.2f}'))
            else:
                troco.append(troco.append(f'{qnt} nota(s) de R$ {nota:.2f}'))
            valor_troco -= qnt * nota
    return troco
def calcula_frete(total, itens, fragil, distancia):
    valor_base = 12.75

    #caixas 
    qntd_caixa = itens // 40
    if itens % 40 !=0 :
        qntd_caixa += 1

    #aliquota
    if fragil == 'S':
        seguro = total * 0.0175
    else:
        seguro = total * 0.008

    v_frete = valor_base + qntd_caixa * 1.82 * distancia + seguro
    return v_frete
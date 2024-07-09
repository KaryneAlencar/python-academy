def calcula_preco_hamburguer(pao, q_carne, salada, bacon, molho, queijo):
    conta = 0
    if queijo == 'S':
        conta += 5.40

    if molho == 'S':
        conta += 1

    if bacon == 'S':
        conta += 7.5

    if salada == 'S':
        conta += 3

    if q_carne == 1:
        conta += 8
    elif q_carne > 1:
        conta += 8 + ((q_carne - 1)*5)
    else:
        conta += 0

    if pao == 'australiano':
        conta += 5.25
    else:
        conta += 7

    if conta > 33:
        desconto = conta * 5/100
        valor_pagar = conta - desconto
        return valor_pagar
    else:
        valor_pagar = conta

        return valor_pagar
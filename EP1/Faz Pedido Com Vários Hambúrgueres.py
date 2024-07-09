def calcula_valor_liquido(valor_pagar, origem):
    if origem == 'pyfood':
        v_liq = valor_pagar - (valor_pagar*0.3)

    else:
        v_liq = valor_pagar - (valor_pagar*0.015) - 7.5
      
    print(f'A hamburgueria ficara com {v_liq:.2f}')
    
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

    else:
        valor_pagar = conta

    print(f'Valor do lanche {valor_pagar:.2f}') #talvez o print saia errado
    return valor_pagar


origem = input('Qual a origem do perdido? [pyfood / whatsapp] ')
valor_total = 0
add_um = input('Deseja inserir um lanche? [S / N] ')
if add_um == 'S':
    verifica = True
    while verifica:
        pao = input('Qual o tipo de pão? Australiano ou Brioche ')
        q_carne = int(input('Qual a quantidade de carne? '))
        salada = input('Deseja salada? [S / N] ')
        bacon = input('Deseja Bacon? [S / N] ')
        molho = input('Deseja molho? [S / N] ')
        queijo = input('Deseja Quejo?[S / N] ')
        
        add_um = input('Deseja inserir um lanche? [S / N] ')
        if add_um == 'N':
            verifica = False
            valor_pagar = calcula_preco_hamburguer(pao, q_carne, salada, bacon, molho, queijo)
            valor_total += valor_pagar

    calcula_valor_liquido(valor_pagar, origem)

    print('Pedido finalizado. Ate mais!')
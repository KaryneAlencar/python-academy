tamanho = input('Qual o tamanho do bolo?')
orcamento = int(input('Qual o orçamento?'))

if tamanho == 'XP':
    preco = 5
    qnt_bolos = orcamento // preco
    troco = orcamento - (preco*qnt_bolos)
elif tamanho == 'P':
    preco = 7
    qnt_bolos = orcamento // preco
    troco = orcamento - (preco*qnt_bolos)
elif tamanho == 'M':
    preco = 20
    qnt_bolos = orcamento // preco
    troco = orcamento - (preco*qnt_bolos)
elif tamanho == 'G':
    preco = 31
    qnt_bolos = orcamento // preco
    troco = orcamento - (preco*qnt_bolos)
else:
    preco = 50
    qnt_bolos = orcamento // preco
    troco = orcamento - (preco*qnt_bolos)

if troco == 0 or troco < 1:
    print('sem acompanhamento')

elif qnt_bolos <= 4:
    if troco % 2 == 0:
        qnt_acompanhamento = troco // 2
        print(qnt_acompanhamento, 'cheesecake')
    elif troco == 1:
        print(1, 'brownie')
    else:
        cheese = troco // 2
        brownie = 1
        print(cheese, 'cheesecake')
        print(1, 'brownie')
else:
    if troco % 2 == 0:
        qnt_acompanhamento = troco // 2
        print(qnt_acompanhamento, 'cupcake')
    elif troco == 1:
        print(1, 'banoffee')
    else:
        cup = troco // 2
        banoff = 1
        print(cup, 'cupcake')
        print(1, 'banoffee')
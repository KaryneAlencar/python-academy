salario = float(input('Qual o salário bruto?'))
dependentes = int(input('Qual o número de dependentes?'))

#inss
if salario <= 1045:
    inss = salario * 0.075
elif salario >= 1045.01 and salario <= 2089.60:
    inss = salario * 0.09
elif salario >= 2089.61 and salario <= 3131.40:
    inss = salario * 0.12
elif salario >= 3134.41 and salario <= 6101.06:
    inss = salario * 0.14
else:
    inss = 671.12

#base
base = salario - inss - dependentes * 189.59

#aliquota e dedução
if base <= 1903.98:
    ali = 0
    ded = 0
elif base >= 1903.99 and base <= 2826.65:
    ali = 0.075
    ded = 142.80
elif base >= 2826.66 and base <= 3751.5:
    ali = 0.15
    ded = 354.80
elif base >= 3751.06 and base <= 4664.68:
    ali = 0.225
    ded = 636.13
else:
    ali = 0.275
    ded = 869.36

#irrf
irrf = base * ali - ded

print(irrf)
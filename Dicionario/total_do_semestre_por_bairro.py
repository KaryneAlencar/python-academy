def total_do_semestre_por_bairro(dic_gastos):
    gasto_ultimos6 = {}
    for bairro, gastos in dic_gastos.items():
        soma = 0
        for i in range(len(gastos) - 6, len(gastos)):
            soma += gastos[i]
        gasto_ultimos6[bairro] = soma
    return gasto_ultimos6

def bairro_mais_custoso(dic_gastos):
    gasto_ultimos6 = total_do_semestre_por_bairro(dic_gastos)
    maior_gasto = 0
    bairro_gasto = ''
    for bairro, gasto in gasto_ultimos6.items():
        if gasto > maior_gasto:
            maior_gasto = gasto
            bairro_gasto = bairro
    return bairro_gasto

def calcula_valor_liquido(valor, origem):
    if origem == 'pyfood':
        v_liq = valor - (valor*0.3)
        return v_liq
    else:
        v_liq = valor - (valor*0.015) - 7.5
        return v_liq
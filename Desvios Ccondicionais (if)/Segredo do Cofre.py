def calcula_segredo(n):
    if n < 100 or n > 999:
        return -1
    else:
        centena = n // 100
        dezena = (n - (centena * 100)) // 10
        unidade = n - (centena * 100) - (dezena * 10)

        soma = centena + dezena + unidade
        return soma
print (calcula_segredo(1000))
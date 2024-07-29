import math

x = 0
dif = 0
maior_erro = 0
while x <= 90:
    seno_b = (4*x*(180 - x))/(40500 - x*(180-x)) #calcula o seno por baskara
    x_rad = math.radians(x)
    seno_n = math.sin(x_rad)
    dif1 = abs(seno_b - seno_n)
    if dif1 > dif:
        dif = dif1
        maior_erro = x
    x += 1
print(maior_erro)


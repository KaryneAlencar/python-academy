qntd = 0
qntd_a = 0
qntd_b = 0
qntd_c =0
qntd_d = 0
qntd_e = 0
qntd_f = 0
verifica = True
while verifica:
    idade = int(input('Qual a idade do paciente? '))
    if idade >= 0 and idade <= 11:
        qntd_a += 1
        qntd += 1
    if idade >= 12 and idade <= 17:
        qntd_b += 1
        qntd += 1
    if idade >=18 and idade <= 25:
        qntd_c += 1
        qntd += 1
    if idade >= 26 and idade <= 35:
        qntd_d += 1
        qntd += 1
    if idade >= 36 and idade <= 59:
        qntd_e += 1
        qntd += 1
    if idade >= 60:
        qntd_f += 1
        qntd += 1
    if idade < 0:
        verifica = False
    

a = (qntd_a/qntd)*100
b = (qntd_b/qntd)*100
c = (qntd_c/qntd)*100
d = (qntd_d/qntd)*100
e = (qntd_e/qntd)*100
F = (qntd_f/qntd)*100

print(f'0-11 anos: {a:.2f} %')
print(f'12-17 anos: {b:.2f} %')
print(f'18-25 anos: {c:.2f} %')
print(f'26-35 anos: {d:.2f} %')
print(f'36-59 anos: {e:.2f} %')
print(f'Acima de 60 anos: {F:.2f} %')


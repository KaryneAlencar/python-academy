v = float(input('Qual a velocidade?'))
teta = float(input('Qual o angulo?'))

import math
g = 9.8
teta = math.radians(teta)
d = (v**2 * math.sin(2*teta))/g

if 98 <= d <= 102:
    print('Acertou!')
elif d < 100:
    print('Muito perto')
else:
    print('Muito longe')
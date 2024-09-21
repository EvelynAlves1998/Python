import math

catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))

#hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
hipotenusa = math.hypot(catetoOposto,catetoAdjacente)

print('o comprimento da hipotenusa é {:.2f}'.format(hipotenusa))
a = int(input(' 1 ° valor: '))
b = int(input(' 2 ° valor: '))
c = int(input(' 3 ° valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
    
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))


#import math --> Ceil - Arrendondar para cima
#floor - Arrendondar para baixo
#trunc - Eliminar o numero da virgula para frente
#pow - calcula a potência de um número
#sqrt - Calcula raiz quadrada
#factorial -  calcular fatorial
from math import sqrt,floor

num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num,floor(raiz)))
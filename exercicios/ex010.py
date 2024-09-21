import math 

n = int(input("Digite um numero: "))
dobro = n*2
triplo = n*3
raizQuadrada = math.sqrt(n) # (n**(1/2))

print('O dobro de {} vale {}\n O triplo de {} vale {}\n A raiz quadrada de {} vale {:.2f}\n'.format(n,dobro,n,triplo,n,raizQuadrada))
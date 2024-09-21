from time import sleep
from random import randint

computador = randint(0,5)

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5,tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO.....')
sleep(3)
if jogador == computador:
    print("Parabéns você venceu!")
else:
    print('Você perdeu eu pensei no numero {}, e você digitou {}!'.format(computador,jogador))
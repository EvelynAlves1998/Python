"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input("Digite um numero:  "))
tot = 0
for c in range(1,num + 1):
    print('\033[33m],end=" "')
    tot += 1
else:
    print('\033[33m],end=" "')
print('\n\033[m0 numero {} foi divisivel {} vezes],end=""'.format(num,tot))
if tot == 2:
    print('Entao ele é primo')
else:
    print('Então não é primo')
"""Crie um programa que faça o computador jogar Jokenpô com você.
GAME: Pedra Papel e Tesoura"""

from random import randint
from time import sleep

itens =('pedra','papel','tesoura')
computador = randint(0,2)

print(""" SUAS OPÇÕES
[0] PEDRA

[1] PAPEL

[2] TESOURA """)

jogador = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print("-=-"*11)
print("O computador escolheu {}".format(itens[computador]))
print("jogador jogou {}".format(itens[jogador]))
print("-=-"*11)

if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE!")
    elif jogador == 2:
        print("COMPUTADOR VENCE!")
    else:
        print("Jogada inválida!")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE!")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE!")
    else:
        print("Jogada inválida!")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE!")
    elif jogador == 1:
        print("COMPUTADOR VENCE!")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada inválida!")

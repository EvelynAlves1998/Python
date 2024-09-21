"""Escreva um programa que leia dois números inteiros e compare-os. 
mostrando na tela uma mensagem:
– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
"""

n1 = int(input("primero numero: "))
n2 = int(input("segundo numero: "))

if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1: 
    print('O segundo valor é maior')
elif n1 == n2:
    print('Os dois são valores iguais')
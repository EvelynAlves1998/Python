
"""Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1,8):
    nasc = int(input("Em que ano a {} pessoa nasceu?:".format(pessoa)))
    idade =atual - nasc
    if idade >= 21:
        totmaior += 1 
    else:
        totmenor += 1
print("Existe {} pessoas maiores de idade".format(totmaior))
print("Existe {} pessoas menores de idade".format(totmenor))
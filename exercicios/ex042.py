salario = float(input("Digite seu salario: "))
"""
Escreva um programa que pergunte o salário de um funcionário 
e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.
"""
if salario >= 1250:
    aumento = salario + (salario * 10 / 100)
    print('Seu salario era {:.2f} e com aumento sera {:.2f}'.format(salario,aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print('Seu salario era {:.2f} e com aumento sera {:.2f}'.format(salario,aumento))
    
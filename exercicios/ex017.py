salario = float(input('Digite o valor do produto: '))
aumentoSalario = salario + (salario * 15)/100
print('O funcionario ganhava R${:.2f}, e com aumento de 15%, passará a receber R${:.2f}'.format(salario,aumentoSalario))

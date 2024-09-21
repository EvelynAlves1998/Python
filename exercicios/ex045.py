"""Escreva um programa para aprovar o empréstimo bancário para a compra 
de uma casa. Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário 
ou então o empréstimo será negado."""

valor_Casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Digite seu salario: "))
pag_anos = int(input("Digite em quantos anos vai pagar a casa: "))

prestacao = valor_Casa / (pag_anos * 12)
minimo = salario_comprador * 30 / 100

print("Para pagar uma casa de R${:2f} em {:.2f} anos".format(valor_Casa,pag_anos))
print("A prestação sera de R${:.2f}".format(prestacao))
print("COMPARANDO tem que pagar {:.2f} e o minimo é de {:.2f}".format(prestacao,minimo))
 
if prestacao <=minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo negado')
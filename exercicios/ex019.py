quantidadeDeKm = float(input("Digite a quantidade de km percorridos: "))
quantidadeDeDias = int(input("Digite a quantidade de dias percorridos: "))

precoAPagar = (quantidadeDeKm * 0.15) + (quantidadeDeDias * 60)
print('O total a pagar é R${:.2f} Reais'.format(precoAPagar))
n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite uma nota: "))

r = (n1+n2)/2

print("A primeira nota do aluno é: {}".format(n1))
print("A segunda nota do aluno é: {}".format(n2))
print("A media entre {} e {} é igual a {:.1f}".format(n1,n2,r))
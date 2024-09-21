numeros = int(input("Digite um numero: "))
# n = str(numeros)

# print("Analisando o numero {}".format(numeros))
# print("Unidade: {}".format(n[3]))
# print("Dezena: {}".format(n[2]))
# print("Centena: {}".format(n[1]))
# print("Milhar: {}".format(n[0]))

#outra forma

u = numeros // 1 % 10
d = numeros // 10 % 10
c = numeros // 100 % 10
m = numeros // 1000 % 10

print("Analisando o numero {}".format(numeros))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))


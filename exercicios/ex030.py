nome = str(input("Digite seu nome completo: "))

print("Seu nome em letras maiusculas: ", nome.upper())
print("Seu nome em letras minuscula: ", nome.lower())
print("Seu nome em letras tem ao todo: ", len(nome))

letras = nome[0:6]
tamanho = len(letras)

print("Seu primeiro nome é {} e ele tem {} letras.".format(letras,tamanho))
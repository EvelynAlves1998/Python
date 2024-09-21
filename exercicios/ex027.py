import random

Aluno1 = str(input("Digite o primero aluno: "))
Aluno2 = str(input("Digite o segundo aluno: "))
Aluno3 = str(input("Digite o terceiro aluno: "))
Aluno4 = str(input("Digite o quatro aluno: "))

lista = [Aluno1,Aluno2,Aluno3,Aluno4]
escolhido = random.shuffle(lista)

print("A ordem de apresentação sera: ")
print(lista)

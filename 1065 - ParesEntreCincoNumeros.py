# beecrowd | 1065
# Pares entre Cinco Números
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

contar_Pares = 0

for _ in range(5):
    numero = int(input())
    
    if numero % 2 == 0:
        contar_Pares +=1
print(f"{contar_Pares} valores pares")
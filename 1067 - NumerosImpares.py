# beecrowd | 1067
# Números Ímpares
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

# Entrada
# O arquivo de entrada contém 1 valor inteiro qualquer.

# Saída
# Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

X = int(input())

cont_impares = 1

if 1 <= X <= 1000:
    while cont_impares <= X:
        if cont_impares % 2 != 0:
            print(f"{cont_impares}")
        cont_impares +=1
            
             
        
# beecrowd | 1044
# Múltiplos
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

# Entrada
# A entrada contém valores inteiros.

# Saída
# A saída deve conter uma das mensagens conforme descrito acima.

a,b = input().split()
a,b = int(a),int(b)

if (a % b == 0) or (b % a == 0):
    print(f"Sao Multiplos")
else:
    print(f"Nao sao Multiplos")
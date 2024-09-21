numero_estrelas = int(input())

estrelas_total = 0
contador = 1

while contador <= numero_estrelas:
    estrelas_total += contador
    contador += 1

print(f'Teremos {estrelas_total} estrelas!')


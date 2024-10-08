
# beecrowd | 1014
# Consumo
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

# Entrada
# O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

# Saída
# Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

distancia_Total = int(input())
litros_Gasto = float(input())

consumo_Medio = distancia_Total/litros_Gasto

print(f"{consumo_Medio:.3f} km/l")
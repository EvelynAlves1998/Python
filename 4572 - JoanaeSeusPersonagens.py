dia,mes,ano = input().split("/")
dia,mes,ano = int(dia),int(mes),int(ano)

soma = dia + mes + ano

if soma % 2 == 0: 
    print("par")
if soma % 2 != 0:
    print("impar")
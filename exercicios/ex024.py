import math

angulo = float(input("Digite um angulo: "))

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print("O angulo tem o valor de {},\n e O valor do seno é {:.2f},\n cosseno é {:.2f}\n e tangente é {:.2f}\n".format(angulo,seno,cosseno,tangente))
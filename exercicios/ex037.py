velocidade = int(input('Digite a velocidade do carro:'))
multa = (velocidade - 80) * 7
if velocidade >= 80:
    print('Você foi multado, porque excedeu o limite de velocidade de 80Km/h! e vai pagar R${} Reais!'.format(multa))
else:
    print('Você esta dentro do limite de velocidade de 80Km/h,então não sera multado!')
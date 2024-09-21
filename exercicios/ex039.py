distancia = int(input('Digite a distância da viagem em Km: '))

print('A viagem tem {} km de distancia!'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor da passagem sera {} Reais!'.format(preço))
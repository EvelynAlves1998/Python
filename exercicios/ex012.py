medida = float(input('Digite uma distancia em metros: '))
print('A medida de', medida,',corresponde a ')
centimetros = medida*100
print('{:.0f}cm'.format(centimetros))
milimetros = medida*1000
print('{:.0f}mm'.format(milimetros))
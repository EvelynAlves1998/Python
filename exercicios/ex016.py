preco = float(input('Digite o valor do produto: '))
desconto = (preco * 5)/100
resultado = preco - desconto
print('O produto custa {:.2f} Reais e o valor ficara {:.2f} reais com 5% de desconto.'.format(preco,resultado))
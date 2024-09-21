n = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(n)) # 'type' Mostra o tipo da variavel
print('So tem espaço? ',n.isspace()) # 'isalpha' Mostra se o valor da variavel tem só tem espaço
print('É numero? ', n.isnumeric()) # 'isnumeric' Mostra se o valor da variavel é tipo int
print('É alfabetico? ', n.isalpha()) # 'isalpha' Mostra se o valor da variavel é tipo str
print('É alfanumerico? ', n.isalnum()) # 'isalnum' Mostra se o valor da variavel é tipo str e int
print('Esta em maiuscula? ', n.isupper()) # 'isupper' Mostra se o valor da variavel esta somente com letras maiusculas
print('Esta em minuscula? ', n.islower()) # 'islower' Mostra se o valor da variavel esta somente com letras minusculas
print('Esta capitalizada? ', n.istitle()) # 'istitle' Mostra se o valor da variavel esta capitalizada

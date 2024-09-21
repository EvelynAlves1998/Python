#Operações com String no Python. 
# As principais operações são o Fatiamento de String, Análise com len(), 
# count(), find(), transformações com replace(), upper(), lower(), 
# capitalize(), title(), strip(), junção com join().

#len() - Comprimento da frase
#count() - Contagem de string especifica
#find() - Quantas vezes encontrou uma string especifica
#in - Verificar se existe alguma string especifica
#replace() - Substituição de string
#upper() - Tranforma a String maiuscula
#lower() - Tranforma a String minusculo
#capitalize() - Transforma caracteres para minuscula e so 1° caracter em maiusculo
#title() - quantas palavras tem uma string analisando os espaços 
#strip() - remove os espaços do inicio e do final de uma string
#rstrip() - remove os espaços do inicio e do final de uma string pelo lado direito
#lstrip() - remove os espaços do inicio e do final de uma string pelo lado esquerdo
#slipt() - Dividi uma string considerando os espaços da string (gera uma lista com todas as palavras dentro de uma cadeia de caracteres)
#join() - Junção de uma strig 

frase = "   Curso em video Python   "

print(frase[1:15]) #imprimi os caracteres com intervalo inicio:fim

print(frase[1:15:2])#inicio:fim:intervalo de n em n caracteres

print(frase[::2]) #':2' pula de 2 em 2

print(frase.count('C'))

print(frase.upper().count('C'))

# print(frase.len(frase))

print(len(frase.strip()))

frase = frase.replace('python', 'android') #troca a palavra python por android
print(frase)

print('curso' in frase)

print(frase.find('Curso'))

print(frase.lower().find('Curso'))

dividido = frase.split()
print(dividido[2][3])



print("""Lorem Ipsum is simply dummy text of the printing and typesetting 
      industry. Lorem Ipsum has been the industry's standard dummy text 
      ever since the 1500s, when an unknown printer took a galley of 
      type and scrambled it to make a type specimen book. 
      It has survived not only five centuries, but also the leap into 
      electronic typesetting, remaining essentially unchanged. 
      It was popularised in the 1960s with the release of Letraset 
      sheets containing Lorem Ipsum passages, and more recently with 
      desktop publishing software like Aldus PageMaker including 
      of Lorem Ipsum.""") #""" para imprimir textos longos


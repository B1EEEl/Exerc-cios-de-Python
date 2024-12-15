#Escreva um programa que verifique se uma palavra é um palíndromo.

#Metodo utilizando for
'''
#leitura da palavra
palavra = input('Digite uma palavra: ').strip() .lower()

#criacão de uma variavel = 0 para depois adicionar valor a ela
palavra_invertida = 0

#for para verificar a quantidade de letras da palavra
for i in range (0, len(palavra)):
#if para ver se a palavra do for é == a palavra ao contrario
    if palavra[i] == palavra[-1-i]:
#adicionamos valor a variavel, agora ela vai aumentando o valor inversamente
        palavra_invertida += 1
    
#if final para saber se é palindromo ou não
if palavra_invertida == len(palavra):
    print('é palindromo')
else:
    print('não é palindromo')

#Segundo modo sem for

if palavra == palavra[:: -1]:
    print('é palindromo')
else:
    print('não é palindromo')
'''

#Utilizando o for, só que agora para frases

# leitura da palavra
palavra = input('Digite uma palavra: ').strip().lower()
if ' ' in palavra:
    palavra = palavra.replace(' ', '')

#criacão de uma variavel = 0 para depois adicionar valor a ela
palavra_invertida = 0

#for para verificar a quantidade de letras da palavra
for i in range (0, len(palavra)):
#if para ver se a palavra do for é == a palavra ao contrario
    if palavra[i] == palavra[-1-i]:

#adicionamos valor a variavel, agora ela vai aumentando o valor inversamente
        palavra_invertida += 1

#if final para saber se é palindromo ou não
if palavra_invertida == len(palavra):
    print('é palindromo')
else:
    print('não é palindromo')
#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

try:
    numero = float(input('Digite um numero aqui: '))

    if numero >=0:
        print('Esse número é positivo')
    else:
        print('esse numero é negativo')
except ValueError:
    print('Apenas Números!')
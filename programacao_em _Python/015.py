#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

try:
    numero = float(input(' Escreva um número aqui: '))
    n1 = (numero % 2) == 0
    if n1:
        print('numero é par')
    else:
        print('esse numero é impar')
except ValueError:
    print('Apenas Números!')
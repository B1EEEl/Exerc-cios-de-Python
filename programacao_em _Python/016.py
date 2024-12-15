#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.

try:
    numero = float(input('Digite um numero: '))
    n2 = float(input('Digite um numero: '))
    if numero==n2:
        print('os numeros são iguais')
    else:
        print('os numeros são diferentes')
except ValueError:
    print('Apenas Números!')
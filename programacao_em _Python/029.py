#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

try:
    numero = int(input('Número: '))

    for mult in range (0,11):
        print(f'{numero} X {mult} = {numero * mult}')
except ValueError:
    print('Apenas Números!')



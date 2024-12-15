#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.

try:
    numero = float(input('Digite aqui um número: '))
    '''
    if numero >=0 and numero <=10:
        print(' esta entre 0 e 10')
    elif numero >=10 and numero <=20:
        print('Está entre 10 e 20')
    else:
        print('é maior que 20')
    '''

    #segundo jeito de fazer

    if numero >20:
        print('maior que 20')
    elif numero >=10:
        print('entre 10 e 20')
    else:
        print('Entre 0 e 10')
except ValueError:
    print('Apenas Números!')
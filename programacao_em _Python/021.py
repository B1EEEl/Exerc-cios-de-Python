#Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).

try:
    numero = int(input('Escreva um numero de 1 a 7: '))

    if numero == 1:
        print('Domingo')
    elif numero ==2:
        print('Segunda-Feira')
    elif numero == 3:
        print('Terça-Feira')
    elif numero == 4:
        print('Quarta-Feira')
    elif numero == 5:
        print('Quinta-Feira')
    elif numero == 6:
        print('Sexta-Feira')
    elif numero == 7:
        print('Sábado')
    else:
        print('Número incorreto')
except ValueError:
    print('Apenas Números!')










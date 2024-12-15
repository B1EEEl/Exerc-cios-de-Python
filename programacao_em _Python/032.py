#Escreva um programa que imprima todos os
# números pares entre dois números fornecidos pelo usuário.
try:
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))

    if inicio < fim:
        for i in range(inicio,fim):
            if i %2 == 0:
                print(i)
    else:
        for i in range(inicio, fim, -1):
            if i % 2 == 0:
                print(i)
except ValueError:
    print('Apenas Números!')

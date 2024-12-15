#Escreva um programa que leia 10 números, se for ímpar deve ser descartado,
#se não, deve ser agregado a uma soma

try:
    soma = 0
    for i in range(1,11):
        n1 = int(input('Numero: '))
        if n1 %2 == 0:
            soma += n1
    print(soma)
except ValueError:
    print('Apenas Números!')





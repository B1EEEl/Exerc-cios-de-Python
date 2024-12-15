#Escreva um programa que calcule a soma dos números de 1 a 100 usando um loop

try:
    soma = 0
    for ele in range (0,101):
        soma = soma + ele
    print(soma)
except ValueError:
    print('Apenas Números!')
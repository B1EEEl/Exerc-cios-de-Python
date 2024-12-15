#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

try:
    menor_peso = None
    maior_peso = None

    for pessoa in range (7):
        peso = float(input(f'Peso: '))
        if maior_peso == None and menor_peso == None:
            maior_peso = peso
            menor_peso = peso

        if peso > maior_peso:
                maior_peso = peso

        if peso < menor_peso:
                menor_peso = peso

    print(f'O menor peso é: {menor_peso}')
    print(f'O maior peso é {maior_peso}')
except ValueError:
    print('Apenas Números!')

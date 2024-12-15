#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000,00
#Qual é o produto mais barato

try:

    soma_preco = 0
    mais_de_mil = 0
    menor_preco = None

    while True:
        produtos = input('Qual produto deseja? {Deseja continuar? [S/N]} ') .upper() [0]
        preco = int(input('O preço desse produto é: '))

        if produtos == 'N':
            break

        if menor_preco == None:
            menor_preco = preco
        elif menor_preco < preco:
            print(f'o menor preço é {menor_preco}')

        soma_preco += preco
    print(soma_preco)


    if preco > 1000:
        mais_de_mil += 1
    print('')
except ValueError:
    print('Apenas Números!')





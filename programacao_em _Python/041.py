#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

try:
    opcao= ''
    soma = 0
    quant = 0
    maior = None
    menor = None

    while opcao != 'Sair':
        n = int(input('Digite um número: '))
        if maior == None and menor == None:
            maior = n
            menor = n

            if n > maior:
                maior = n
            if n < menor:
                menor = n

    #Soma
    soma += n
    #quant_Ciclos
    quant += 1

    opcao = input('Deseja continuar? [Sair para Parar]: ')

    print(f'A media é {soma/quant}'
          f'\n O maior número é {maior}'
          f'\nO menor número é {menor}')
except ValueError:
    print('Apenas Números!')
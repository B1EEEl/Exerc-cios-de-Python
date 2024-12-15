#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário

try:
    #Leitura de dados
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    cidade = input('Qual cidade você nasceu: ')
    # Retorno ao usuário
    print(f'Meu nome é {nome}, tenho {idade} anos e nasci em {cidade}')
except ValueError:
    print('Apenas números')


#Escreva um programa que leia o nome, e o sobrenome, CONCATENE em uma nova variável nome completo, e retorne para o usuário

#leitor de nome e sobrenome
nome = input('Digite seu nome: ')
sobrenome = input('Digite Seu Sobrenome: ')

#"calculo" para juntar nome e sobrenome
nome_completo = nome + ' ' + sobrenome

#Retorno ao usuário
print(f'Meu nome completo é: {nome_completo}')
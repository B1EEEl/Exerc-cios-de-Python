#Crie um programa que leia um nome, e mostre o primeiro e o último nome

#Leitura de dados
nome = input('Digite aqui o seu nome completo: ').strip()

#achar o primeiro nome
espaco_nome= nome.find(' ')
primeiro_nome= print(nome[:espaco_nome])

#achar o ultimo nome
ultimo_espaco = nome.rfind(' ')
ultimo_nome = print(nome[ultimo_espaco + 1:])
#"rfind" essa variável começa com um "r" pois ela começa a ler o programa, frase ou nome pela direita!
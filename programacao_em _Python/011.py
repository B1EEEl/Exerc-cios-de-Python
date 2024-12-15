#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar os espaços)
#Quantas letras tem o primeiro nome


#Entrada de Dados
nome_completo = input('Digite o seu nome completo: ').strip()

#1
print(nome_completo)

#2
print(nome_completo.upper())

#3
print(nome_completo.lower())

#4
sem_espaco = nome_completo.replace(' ', '')
print(len(sem_espaco))

#5
#Neste exercicios, utilizamos a tatica do "find" para achar o primeiro espaço.
#para depois contabilizar o primeiro nome até essse espaço achado
espaco = nome_completo.find(' ')
letras_1_espaco = len(nome_completo[:espaco])
print(letras_1_espaco)




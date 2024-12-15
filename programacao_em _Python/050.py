#Escreva um programa que leia uma frase,
#e mostre uma formatação adaptável de acordo com o tamanho da frase, coordenado por uma função


def mensagem(palavra):
    print('-' * (len(palavra) * 2))
    print(f'{palavra.center(len(palavra) * 2 )}')
    print('-' * (len(palavra) * 2))
palavra = input('Digite uma mensagem: ')
mensagem(palavra)









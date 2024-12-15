#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10
# e continue pedindo até que o usuário acerte o número.
# E no final, retorne também a quantidade de tentativas necessárias.
import random
tentativa = 0
escolha = ''
numero = random.randint(1,11)
while escolha != numero:
    escolha = int(input('Número '))

    if numero == escolha:
        print(f'Parabéns, você acertou. Seu numero foi {escolha}, e o do pc foi {numero}')
    else:
        print('Tente novamente')

    if numero != escolha:
        tentativa += 1

print(f'o numero de tentativas foi {tentativa}')


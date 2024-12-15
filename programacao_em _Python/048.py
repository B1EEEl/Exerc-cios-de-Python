#Crie um programa que pede ao usuário para digitar dois números e, em seguida,
#divida o primeiro número pelo segundo número. No entanto, o programa deve ser capaz de lidar
#com a possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.

#ZeroDivisionError ; ValueError
'''
try:
    n1= int(input('Número: '))
    n2= int(input('Número: '))

    divisao = n1 / n2
    print(f'O resultado da divisão é: {divisao}')

except ValueError:
    print('Apenas números')
except ZeroDivisionError:
    print('Não pode ser dividio por 0')
'''


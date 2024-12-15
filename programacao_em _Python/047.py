#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.

#Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

try:

      valor_saque = int(input('Qual valor deseja sacar: '))


      cedulas_50 = valor_saque // 50
      valor_saque = valor_saque % 50

      cedulas_20 = valor_saque // 20
      valor_saque = valor_saque % 20

      cedulas_10 = valor_saque // 10
      valor_saque = valor_saque % 10

      cedulas_1 = valor_saque // 1
      valor_saque = valor_saque % 1

      print(f'Quantidade de cédulas de 50 {cedulas_50}'
            f'\nQuantidade de cédulas de 20 {cedulas_20}'
            f'\nQuantidade de cédulas de 10 {cedulas_10}'
            f'\nQuantidade de cédulas de 1 {cedulas_1}')
except ValueError:
    print('Apenas Números!')
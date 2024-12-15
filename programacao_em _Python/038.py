#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
#1.	Somar
#2.	Multiplicar
#3.	Maior
#4.	Novos números
#5.	Sair do programa

try:
    opcao = ''
    while opcao != '5':
        print('--------------------------------')
        numero1 = int(input('Numero: '))
        outro_numero1 = int(input('Numero: '))
        outro_numero2 = int(input('Numero: '))

        opcao = input('O que deseja?'
                      '\n1 - Somar'
                      '\n2 - Multiplicar'
                      '\n3 - Maior'
                      '\n4 - Novos números '
                      '\n5 -  Sair do programa ----> ')
        if opcao == '1':
            print(f'A soma é {numero1 + outro_numero1 + outro_numero2}')

        elif opcao == '2':
            print(f'A multiplicação é {numero1 * outro_numero1 * outro_numero2}')

        elif opcao == '3':
           if numero1 > outro_numero1 and numero1 > outro_numero2:
            print(f'O maior número é o número {numero1} ')

           elif outro_numero1 > numero1 and outro_numero1 > outro_numero2:
               print(f'O maior número é o número {outro_numero1}')
           else:
               print(f'O maior número é o numero {outro_numero2}')

        elif opcao == '4':
            numero1 = int(input('Numero: '))
            outro_numero1 = int(input('Numero: '))
            outro_numero2 = int(input('Numero: '))

        elif opcao == '5':
            print('Até breve')


        else:
                print('Você saiu do programa')
except ValueError:
    print('Apenas Números!')
#Simulação de um Caixa Eletrônico Este programa simula
# um caixa eletrônico, permitindo que o usuário faça depósitos,
# saques e consulte o saldo da conta, e sair

try:

    opcao = ''
    saldo = 0

    while opcao != '4':
        print('<------------>')
        opcao = input('O que deseja?'
              '\n1-Fazer um Depósito '
              '\n2-Sacar dinheiro'
              '\n3-Consultar saldo'
              '\n4-Sair ---->')
        if opcao == '1':
            deposito = float(input('Quanto deseja Depositar? '))
            saldo += deposito
        elif opcao == '2':
            saque = float(input('Quanto deseja sacar? '))
            saldo -= saque
            if saldo < saque:
                    print('Impossível pois o seu o saque que o Senhor quer fazer, é maior do que o valor do saldo!')
            else:
                print('Valor sacado')
        elif opcao == '3':
            print(f'O seu Saldo é de: {saldo}')

        elif opcao == '4':
            print('Até logo, Volte sempre')

        else:
            print('Opção Inválida')
except ValueError:
    print('Apenas Números!')
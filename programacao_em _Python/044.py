#Crie um programa para jogar par ou ímpar com o usuário,e só pare quando perder.
# Ao final deve mostrar a quantidade de vitórias

try:
    quant = 0

    import random



    while True:
        escolha = input('esolhe par ou ímpar? [P/I]').upper()[0]
        n = int(input('Número: '))
        pc = random.randint (0,10)
        resultado = pc + n

        if resultado == (pc % 2) == 0 and escolha == 'P' or resultado != (resultado % 2) == 0 and escolha == 'I':
            print(f'{n} + {pc} = {n + pc} --> Vitória')
            quant += 1
        else:
            print(f'{n} + {pc} = {n + pc} --> Derrota. Você ganhou {quant} vezes')
            break
except ValueError:
    print('Apenas Números!')
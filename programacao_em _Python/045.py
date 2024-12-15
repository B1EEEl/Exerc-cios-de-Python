#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000

try:

    '''
    soma = ''
    while True:
        n = input('Número: ')
    
        if n == '0000':
            break
        soma = int(n)
        for mult in range(0, 11):
            print(f'{soma} X {mult} = {soma * mult}')
    '''

    while True:
        n = input('Número: ')

        if n == '0000':
            break
        for mult in range(0, 11):
            print(f'{int(n)} X {mult} = {int(n) * mult}')
except ValueError:
    print('Apenas Números!')


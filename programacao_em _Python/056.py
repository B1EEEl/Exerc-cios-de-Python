#Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze')
try:
    while True:
        numero = int(input('Digite um número de 0 à 15: '))
        print(numeros[numero])
except ValueError:
    print('apenas numeros')
except IndexError:
    print('Somente nu'
          'meros entre 0 e 15')
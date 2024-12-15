

#Faça um programa que leia um número e retorne o fatorial !
#4! = 4 x 3 x 2 x 1

try:

    n1 = int(input('Digite o número: '))
    fat = 1
    while n1 != 1:
        fat = fat * n1
        n1 = n1 - 1
        print(n1, fat)


    '''
    n = int(input('Digite o número: '))
    fat = 1
    c = 1
    while c != n:
        c = c + 1
        fat = fat * c
    
    print(fat)
     '''
except ValueError:
    print('Apenas Números!')


#Crie uma função para verificar se um número é par ou ímpar

'''
def numero(n):
    if (n % 2) == 0:
        print(f'Você escolheu, {impar_ou_par} e este número é par!!!')
    else:
        print('É ímpar!')
impar_ou_par = int(input('Número: '))
numero(impar_ou_par)
'''
def impar_par(n):
    return 'P' if n % 2 == 0 else 'I'

def area(a,b):
    return a*b

def volume (a,b,c):
    return area(a,b) * c
print(volume(5,7,10))



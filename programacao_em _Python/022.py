#Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média,
#é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).

try:
    n1 = float(input('Digite o valor da nota n1: '))
    n2 = float(input('Digite o valor da nota n2: '))
    n3 = float(input('Digite o valor da nota n3: '))
    n4 = float(input('Digite o valor da nota n4: '))
    n5 = float(input('Digite o valor da nota n5: '))
    n6 = float(input('Digite o valor da nota n6: '))

    nota = (n1 + n2 + n3 + n4 + n5 ) / 5

    if nota >= 9:
        print('Nota excelente, está aprovado')
    elif nota > 7:
        print('Boa nota, está aprovado')
    elif nota >= 6:
        print('Nota suficiente para passar, está aprovado')
    else:
        print('Tente na proxima, reprovou!')
except ValueError:
    print('Apenas Números!')









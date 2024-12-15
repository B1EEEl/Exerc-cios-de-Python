#Crie um programa que tenha a função área(),
#que receba as dimensões de um muro retangular e mostra a área do terreno


def area(a, b):
    return a * b
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

print(area(largura, comprimento))

#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois, deve mostrar para cada palavra, suas vogais

palavra = ('amor', 'sentido', 'castelo', 'coloracao','analista')
for ele in palavra:
    print(ele, end='-')
    for i in ele:
        if i in 'aeiou':
            print(i,end=',')
    print()


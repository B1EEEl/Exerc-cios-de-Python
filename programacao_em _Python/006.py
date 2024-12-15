#Escreva um programa que leia 6 notas diferentes e faça a média do aluno
try:
    #Leitor de notas
    n1 = float(input('Digite o valor da nota n1: '))
    n2 = float(input('Digite o valor da nota n2: '))
    n3 = float(input('Digite o valor da nota n3: '))
    n4 = float(input('Digite o valor da nota n4: '))
    n5 = float(input('Digite o valor da nota n5: '))
    n6 = float(input('Digite o valor da nota n6: '))

    #Cálculo para realização da média
    media = (n1 + n2 + n3 + n4 + n5 + n6) / 6

    #Retorno para o usuário
    print(f' A sua média final é : {media} ')
except ValueError:
    print('Apenas numeros para as notas')
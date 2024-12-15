#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

try:
    #Leitura do numero
    numero = float(input("digite o valor do numero: "))

    #Realização das contas
    dobro_numero = numero * 2
    triplo_numero = numero * 3
    raiz_quadrada = numero ** (1/2)


    #Saída de dados
    print(f'o dobro de {numero} é: {dobro_numero} '
          f'\no triplo de {numero} é : {triplo_numero} '
          f'\nraiz Quadrada de {numero} é : {raiz_quadrada}')
except ValueError:
    print('apenas números para calcular')
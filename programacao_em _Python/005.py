#Escreva um programa que converta real para o Franco Congolês

try:
    #Leitor de Reais
    reais = float(input('Digite a quantidade de reais que deseja converter: '))

    #Cálculo
    reais_final = reais / 0.0019

    #Saída de Dados10
    print(f'10,00 reais, equivalem a {reais_final:.2f} Francos Congoleses')
except ValueError:
    print('Apenas numeros para os calculos')
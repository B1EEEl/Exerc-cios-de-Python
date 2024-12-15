#Crie um programa para analisar o IMC de uma pessoa
#, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

try:
    peso = float(input('Digite quantos kg você tem: '))
    altura = float(input('Digite quantos metros você tem: '))
    altura_quadrado = altura * altura

    imc = peso / altura_quadrado
    if imc < 18.5:
        print(f'Abaixo do Peso normal')
    elif imc ==18.5 and imc < 24.9:
        print(f'Peso Normal! seu IMC é de {imc}')
    elif imc ==25 and imc <=29.9:
        print(f'Excesso de peso! seu IMC é de {imc}')
    elif imc == 30 and imc <= 34.9:
        print(f'Obesidade Classe 1! seu IMC é de {imc}')
    elif imc == 35.0 and imc <= 39.9:
        print(f'Obesidade classe 2! seu IMC é de {imc}')
    else:
        print(f'Obesidade classe 3! seu IMC é de {imc}')
except ValueError:
    print('Apenas Números!')
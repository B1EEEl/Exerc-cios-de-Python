#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.

try:
    #leitura de dados
    salario = float(input(('Digite aqui o valor do seu salário: ')))

    #realização das contas
    reajuste = salario * 60 / 100
    reajuste_positivo = salario + reajuste

    #Retorno ao usuario
    print(f'O salário de {salario} com o reajuste de 60% será de : {reajuste_positivo}')
except ValueError:
    print('Apenas numeros')





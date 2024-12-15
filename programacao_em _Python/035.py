#Escreva um programa que leia o
#Nome, idade e sexo de 4 pessoas. No final mostre:

#A média de idade do grupo
#Qual é o homem mais velho
#Quantas mulheres têm menos de 20 anos
try:
    soma_idade = 0
    mulher_20_anos = 0
    maior_idade = None


    for pessoas in range(4):
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        sexo= input('Sexo [M/F]: ').upper().strip()[0]

        #Média de idade
        soma_idade += idade

        #Homem mais velho
        if sexo == 'M' and maior_idade == None:
            maior_idade = idade

        elif sexo == 'M' and maior_idade > idade:
            nome_homem_mais_velho = nome
            maior_idade = idade

        #Mulheres menos de 20 anos
        if sexo == 'F' and idade < 20:
            mulher_20_anos += 1

    print(f'A média de idades é: {soma_idade / 4}')
    print(f'Idade do homem mais velho é: {maior_idade}')
    print(f'Quantidade de mulheres com menos de 20 anos é: {mulher_20_anos}')
except ValueError:
    print('Apenas Números!')





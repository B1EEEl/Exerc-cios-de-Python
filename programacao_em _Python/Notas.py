# Print e Saída de Dados
'''
print('Olá Mundo')

# Operações Básicas
print(3 + 3)
print(8 - 999999)
print(898965897 / 9)
print(6 ** 24)
print(3 % 2)


Idade = 45
soma_idades = 6 + 10
idade_joao = 70
idade_maria = 8
soma_joao_maria = idade_joao + idade_maria
print(soma_joao_maria)

#print formatado
print(f'A soma de idades é {soma_joao_maria}')


#Entrada de dados
nome = input('Digite seu nome: ')
print(f'Seu nome é {nome}')
'''
'''
idade = int(input('Digite a sua idade: '))
idade_final = idade + 989
print(idade_final)


#Concatenação

Nome = 'Gabriel'
Sobrenome = 'Faria'
Nome_completo = Nome + Sobrenome
print(Nome_completo)
'''

'''
#9 - Escreva um programa que leia um tipo de dado e usando a
# função type(), retorne ao usuário, qual o tipo de dado informado

dado = input('digite algo: ')
print(type(dado))

#print(type (1))
#print(type(1.5))
#print(type('a'))

#10 - Escreva um programa que leia um tipo de dado e usando um método .isnumeric(), retorne ao usuário

dado = input('Digite algo: ')
print(type(dado))
print(dado.isnumeric())


#Strings

nome = 'Luis Eulalio'

#Fatiamento
print(nome[0])
print(nome[0:6])
print(nome[5: ])

#Análise
print(len(nome))
print(nome.count('a'))
print(nome.find('l'))

#Transformação
print(nome.upper())
print(nome.lower())
print(nome.capitalize())
print(nome.replace('l', 'oi'))


Nome = input('Digite Seu nome: ') .strip()
print(Nome)

# Estruturas condicionais: If, Else e Elif
altura = float(input('Coloque sua altura: '))

if altura > 1.3:
    print('Pode andar tranquilamente')
else:
    print('Quem sabe ano que vem')

#Programa Utilizando o Elif
if altura > 3:
    print('Cuidado vai bater a cabeça')
elif altura < 1.3:
    print('Quem sabe no ano que vem')
else:
    print('pode andar')

#Programa ultizando coniçoes estruturais e agora string's
nome = 'Luis Tatin'
if nome == 'João da Silva':
    print ('tá liberado')
else:
    print('Nome incorreto')
'''
'''
#função aleatório
import random
#variavel
aleatorio = random.randint(1, 10)
print(aleatorio)
'''
'''
#Nova bibloteca, o import time, ele adiciona um tempo que você escolhe qual o tempo, em segundo

import random
import time
pc = int(input("Digite um numero de 1 à 3: "))
jokempo = random.randint(1,3)
print('JO')
time.sleep(2)
print('KEM')
time.sleep(2)
print('PO')
time.sleep(2)

if pc == jokempo:
    print('Empate')

elif (jokempo == 1 and pc == 2) or ( jokempo == 1 and pc == 3) or (jokempo == 2 and pc == 38):
    print('Você ganhou')
else:
    print('Você perdeu')
'''
'''
#laços de Repetição - "FOR"

for ele in range (0,10):
    print("*")
'''
'''
for ele in range (0, 10):
    print(ele)

for ele in range (10,0,-1):
    print(ele)

soma = 0
for ele in range (0,11):
    soma = soma + ele
print (soma)
'''
'''

contador = 0

while contador < 100:
    print('*')
    contador +=1
'''
'''
#caso 2
decisao = ''
while decisao != 'N':
    numero = int(input('Número: '))
    if numero %2 == 0:
        print('par')
    decisao = input('Deseja continuar? [S/N]: ').upper() .strip() [0]


#caso 3
opcao = ''
while opcao != 'Sair':
    numero = int(input('Número: '))
    outro_numero = int(input('Número: '))

    opcao = input('O que deseja? \n'
                  '1- Somar \n'
                  '2- Multiplicação \n'
                  'Sair ----------->')


    if opcao == '1':
        print(f'A soma é: {numero + outro_numero}')
    elif opcao == '2':
        print(f'A multiplicação é: {numero * outro_numero}')
    else:
        print('Erro')


a = 0
while True:
    respostas = input('Quer mais números? {S/N} ').upper()[0]
    if respostas == 'N':
        break
    else:
        for i in range (100):
            a += 1
            print(a)

try:
    numero = int(input('Número: '))
    numero = numero / 0
except ValueError:
    print('Apenas números')
except:
    print('Error: Chamar o TI')
'''

#Funções
'''
def bem_vindo():
    print('-' * 50)
    print('Bem Vindo ao Senai!!!')
    print('-' * 50)
bem_vindo()

def mensagem(msg):
    print('*' * 50)
    print(f'{msg}!!!!!')
    print('*' * 50)

mensagem('Bem-Vindo')

def volume(r):
    return (4/3) * 3.1415 * r ** 3
volume_esfera = volume(7)
print(volume_esfera)

'''
'''
#Tuplas
carro = ('Ferrari', 'Vermelha', '2023')
print(carro)
print(carro[0])
print(sorted(carro))

for ele in carro:
    print(ele)

print(carro.index('2023'))

idades = (10,45,23,67)
print(max(idades))
print(min(idades))
print(sum(idades) / len(idades))
'''

'''
#Listas
carro = ['Ferrari', 'Vermelha', '2023']

carro.append('785 CV')
carro.insert(1,'Gasolina')
carro.remove('Gasolina')
carro.pop(0)


for i in carro:
    print(i)
'''

lista = []

while True:
    numero = input('Número: ')
    if numero == '0000':
        break
    lista.append(int(numero))

print(f'{max(lista)} {min(lista)} {sum(lista)/len(lista)} ')






















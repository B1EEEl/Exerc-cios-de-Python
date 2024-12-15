#Crie um programa que leia vários números inteiros.
# O programa só vai parar quando o usuário digitar 0000.
# No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)

tentativas = 0
soma = 0

while True:
    respostas = input('Número: ')

    if respostas == '0000':
        break

    soma += int(respostas)
    tentativas += 1

print(f'o numero de tentativas foi: {tentativas}')
print(soma)



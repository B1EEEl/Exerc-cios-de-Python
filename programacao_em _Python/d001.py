#Escreva um programa que execute o cálculo da Função horária da posição no MRUV,
# e retorne de acordo com o tempo informado pelo usuário
#s=si+vi*t + a.t**2/2
# s= posição
# si = posição inicial
# vi = velocidade inicial
# a = aceleração
# t = tempo

try:

    #Leitura de dados (informações da conta)
    si = float(input(('Digite a posição do seu corpo: ')))
    vi = float(input('Digite a velocidade inicial do seu corpo: '))
    a = float (input('Digite o valor da aceleração do seu corpo: '))
    t = float(input('Digite o valor do tempo: '))

    #Realização da conta
    S = si + vi * t + (a * (t ** 2)) / 2

    #Retorno ao usuário
    print(f' posição do objeto no tempo {t} é de {S} ')
except ValueError:
    print('Apenas Números!')


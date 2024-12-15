#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
#V = (4/3) . π . r³
#A = 4 . π . r²

try:
    #Leitor do raio
    raio = float(input('digite o valor do seu Raio do volume: '))

    #Cálculo de área e volume
    volume = ((4 * 3) * 3.1415 * (raio **3) )
    area = (4 * 3.1415 * (raio**2))

    #retorno ao usuário
    print(f'Volume da esfera: {volume:.2f} \nÁrea da esfera: {area:.2f} ')
except ValueError:
    print('APenas números para calculos')


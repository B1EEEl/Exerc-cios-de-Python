#Crie um programa que verifica se uma pessoa pode ser doadora de sangue,
# considerando a idade e os critérios de saúde.
#idade
#peso
#sono#vacina

try:
    idade = int(input('Idade: '))
    if idade >= 16 and idade <= 69:
        peso = float(input('Peso: '))
        if peso > 50:
            sono =int(input('Quantas horas dormiu nas ultimas 24 horas? '))
            if sono >= 8:
                vacina = input('Suas vacinas estão em dia? [S/N] ')
                if vacina == 'S':
                    print('Pode se vacinar')

                else:
                    print('Coloque as vacinas em dia, não pode se vacinar')

            else:
                print('Dormiu pouco!')

        else:
            print('Peso incorreto')

    else:
        print('Idade incorreta')
except ValueError:
    print('Apenas Números!')
#Crie um programa para jogar JOKEMPO, usando a função random.randint

try:

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
except ValueError:
    print('Apenas Números!')






'''
if jokempo == 1 and pc == 1:
    print(f'Empate pois maquina jogou {jokempo} e jogador jogou {pc}')
elif jokempo == 1 and pc == 2:
    print(f'Jogador ganhou!pois maquina jogou {jokempo} e jogador jogou {pc}')
elif jokempo == 1 and pc == 3:
    print(f'Pc ganhou!pois maquina jogou {jokempo} e jogador jogou {pc}')
elif jokempo == 2 and pc == 1:
    print(f'maquina ganhou pois maquina jogou {jokempo} e jogador jogou {pc}')
elif jokempo == 2 and pc == 2:
    print(f'Empate pois maquina jogou {jokempo} e jogador jogou {pc}')
elif jokempo == 2 and pc == 3:
    print(f'Pc ganhou pois maquina jogou {jokempo} e jogador jogou {pc}')
elif jokempo == 3 and pc == 1:
    print(f'Maquina ganhoupois maquina jogou {jokempo} e jogador jogou {pc}')
elif jokempo == 3 and pc == 2:
    print(f'Maquina ganhou pois maquina jogou {jokempo} e jogador jogou {pc}')
elif jokempo == 3 and pc == 3:
    print(f'Empate pois maquina jogou {jokempo} e jogador jogou {pc}')
else:
    print("coloque apenas numeros de 1 à 3")
'''
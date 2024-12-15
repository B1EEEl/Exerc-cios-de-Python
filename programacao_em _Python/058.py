#Crie um programa onde serão informados diversos valores em uma lista.
# Caso o número já exista ele não será adicionado. No final,
# serão exibidos todos os valores únicos em ordem crescente

lista = []
while True:
    try:
        numero = input('Numero: ')
        if numero == '0000':
            break
        if int(numero) not in lista:

            lista.append(int(numero))
    except ValueError:
        print('Apenas números')
print(f'{sorted(lista)}')

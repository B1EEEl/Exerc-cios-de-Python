#Escreva um programa que crie uma lista com os números de 1 a 10 e,
# em seguida, exiba apenas os números pares da lista.

lista = [x for x in range(1,11) if x % 2 == 0]
print(lista)

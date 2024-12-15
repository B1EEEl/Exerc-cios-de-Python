#Escreva um programa que calcule a soma de todos
#os números múltiplos de 4 que são encontrados entre 1 até 500

soma = 0
for i in range(0, 501, 4):
    soma += i
print(soma)

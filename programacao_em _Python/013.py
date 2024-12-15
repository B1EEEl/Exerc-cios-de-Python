#Crie um programa que leia uma frase e mostre:
#1.Quantas vezes aparece a letra “a”
#2.Em que posição ela aparece a primeira vez
#3.Em que posição ela aparece na última vez

#Entrada de dados
frases = input('Digite aqui a sua frase: ').strip() .lower()
frases = frases.replace('ã','a')
frases = frases.replace('á','a')
frases = frases.replace('à','a')
frases = frases.replace('â','a')
frases = frases.replace('A','a')

#1.Quantas vezes aparece a letra “a”
print(frases.count('a'))

#2.Em que posição ela aparece a primeira vez
print(frases.find('a')+1)

#3.Em que posição ela aparece na última vez
print(frases.rfind('a')+1)





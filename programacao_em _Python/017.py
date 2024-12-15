#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
letra = input('Digite aqui alguma letra: ').strip().lower()

if letra in 'aeiouáàâãéèêìíîóòôõúùû':
    print('é uma vogal!!')
else:
 print(' é uma consoante')
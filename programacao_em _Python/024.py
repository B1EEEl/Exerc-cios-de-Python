#Escreva um programa que peça ao usuário uma
# senha e verifique se ela está correta (a senha correta é "python123").

senha = input("Digite uma senha: ")

if senha != "python123":
    print("Senha incorreta!")
else:
    print("Senha correta!")
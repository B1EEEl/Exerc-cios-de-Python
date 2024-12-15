#Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

#1-Apenas os 3 primeiros mais assistidos
#2-Os últimos 2 mais assistidos
#3-A lista em ordem alfabética
#4-Em que posição está “O rei leão”

filme = ('Avatar','Vingadores: Ultimato','Avatar: O Caminho da Água','Titanic ','Star Wars: O Despertar da Força','Vingadores: Guerra Infinita','Homem-Aranha: Sem Volta Para Casa ','Jurassic World','O Rei Leão', 'Os Vingadores')
print(filme[0:3])
print(filme[8:10])
print(sorted(filme))
print(filme.index('O Rei Leão'))

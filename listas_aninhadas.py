"""
Listas Aninhadas

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais(Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as listas

numeros = [1, 2, 3, 4, 5]

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(type(listas))
print(listas)

# Como fazemos para acessar os dados?

print(listas[1][1])

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]
print([valor for valor in listas])

"""

# Outros exemplos

# Gerando um tabuleiro/matrix 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valor inicial

print([['*' for i in range(1, 4)] for j in range(1, 4)])
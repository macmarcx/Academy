"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anônimas.

# Função em Python

def soma(a, b):
    return a + b

# Exemplo de função em Python
def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# Expressão Lambda

lambda x: 3 * x + 1

# E como utilizar a expressão lambda?

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

"""

# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('marcos', 'silva'))

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também

amar = lambda: 'Como não amar Python? '
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ..., xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))
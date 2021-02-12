"""
Entendendo o *args

- O *args é um parâmetro, como qualquer outro. Isso significa que você poderá
chamar de qualquer coisa, desde que começe com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))


def soma_todos_numeros(*args):
    print(args)
    return sum(args)

soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(3, 4)
soma_todos_numeros(4, 5, 2)
soma_todos_numeros('Marcos')
"""

# Entendendo o args

def soma_todos_numeros(*args):
    print(args)
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador
# Aqui estamos passando uma lista, e ao utilizar o '*' estamos transformando essa lista em tupla
print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar estes dados.
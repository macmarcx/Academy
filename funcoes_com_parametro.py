"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

"""

def quadrado(numero):
    quad = numero * numero
    return quad

print(quadrado(10))

def outro(valor1, valor2, msg):
    res = (valor1 * valor2) * msg
    return res

print(outro(3, 4, 'Marcos '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

def nome_completo(nome, sobrenome):
    dados = [nome, sobrenome]
    return dados

print(nome_completo('marcos', 'silva'))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(sobrenome='Angelina', nome='Jolie'))
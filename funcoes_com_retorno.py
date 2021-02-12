"""
Funções com retorno



# Exemplo função

def quadrado_de_7():
    res = 7 * 7
    print(res)
    return res

def soma_simples(a, b):
    soma = a + b
    return soma

resultado = soma_simples(quadrado_de_7(),10)

print(resultado)

result = quadrado_de_7()

soma = result + 1

print(soma)

"""

# Vamor criar uma função para jogar a modeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
            return 'cara'
    return 'Coroa'

print(joga_moeda())
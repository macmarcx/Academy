"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University)

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TyperError
# Colocando na variavel potencia um valor padrão, caso o usuário não digite o
# segundo valor.

def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))    # 2 * 2 * 2 = 8
print(exponencial(3, 2))    # 3 * 3 = 9

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3, 5)) # Eleva á potência informada pelo usuário

# OBS: Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro numero, e será calculado o quadrado
# deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro numero e o segundo ao parâmetro potencia.
# Então será calculada esta potência.

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

def teste(potencia, num=2):
    return num ** potencia

print(teste(6))
"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variavel

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()
print(fora())
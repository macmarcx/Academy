"""
Escopo de variáveis

Dois casos de escopo:

1 - Variaveis globais:
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variaveis locais:
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada.

Para declarar vairiaveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que ao declarar uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

# Variavel global
numero = 42
print(numero)
print(type(numero))

if numero > 10:
    # Variavel local
    novo = numero + 10
    print(novo)


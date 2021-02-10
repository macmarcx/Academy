"""
Loop While

Forma geral

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleanda for verdadeira.

Expressãõ Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5

# Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero += 1

# OBS: Em um loop while, é importante que cuidemos do critério de parada.

"""

# Exemplo 2

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou? ')
    if resposta == 'não':
        print('Continue...')
    elif resposta != 'sim' and 'não':
        print("Essa mensagem é invalida, digite 'sim' ou 'não'")
    else:
        print("Acabou o processo")

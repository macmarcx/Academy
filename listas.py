"""
Listas

Listas em Python funciona como vetores/matrizes(arrays) em outras linguagens, com a diferença
de serem dinâmicos e também de podermos colocar QUALQUER tipo de dado.

Em Python:

- Dinâmico: Não possui tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- QUalquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo dado.

As listas em Python são representadas por colchetes: []

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['M', 'a', 'r', 'c', 'o', 's', 's', 'i', 'l', 'v', 'a']

lista3 = []

lista4 = list(range(11))

lista5 = list('Marcos Silva')

lista6 = ['marcos', 'silva', 'antonio', 'marcela']

# Podemos facilmente checar se determinado valor está contido na lista

while True:
    nome = input("Digite seu nome: ")
    if nome in lista6:
        print(f"O {nome.capitalize()} está na lista")
        break
    else:
        print(f"O nome {nome} não foi encontrado, você digitou certo? ")

# print(lista6[2].upper())

# Podemos facilmente ordenar uma lista
lista6.sort()
print(lista6)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('a'))

# Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
lista1.append(12, 34, 56) Erro
lista1.append([12, 34, 56]) Certo

print(lista1)
lista1.append([8, 3, 1])
print(lista1)


Para extender uma lista, utilizamos a função extend

Ele adiciona somemte uma lista de dados

lista1.extend([14, 11, 45])
print(lista1)

# Podemos inserir um elemento na lista informando a posição do indice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista

lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente inverter uma lista
# Forma 1
lista1.reverse()
print(lista1)

# Forma 2
print(lista1[::-1]) #slice

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos conta quanto elementos existem dentro da lista

print(len(lista4))

# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o último elemento, mas também o retorna

print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos à direita deste indice serão deslocados para a esquerda.
# OBS: Se não houver elemento no indice informado, teremos um erro IndexError.

lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)

print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2

curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista7 = [1, 2, 34, True, 'Marcos', 'd', [1, 2, 3], 16525635165]
print(lista7)

# Iterando sobre listas

# Exemplo 1

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#           0         1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazemos acesso aos elementos de forma indexada inversa

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde

for cor in cores:
    print(cor)

indice = 0

while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# Outros métodos não tão importantes, mas também uteis

# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 5,  8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual indice está o valor 9?
print(numeros.index(9))

# OBS: Caso não tenha este elemento na lista, será apresentando erro ValueError

# OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer uma busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1)) # Buscando a partir do indice 1
print(numeros.index(5, 2)) # Buscando a partir do indice 2

# OBS: Podemos fazer a busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) # Buscar o indice do valor 8,  entre os indices 3 a 6

# Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:3:2]) # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro "fim"

print(lista[:2]) # começa em 0, pega até o indice 2 - 1

print(lista[:4]) # começa em 0, pega até o indice 4 - 1

print(lista[1:3]) # começa em 1, pega até o indice 3 - 1

# Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2]) # começa em 1, vai até o final, de 2 em 2

print(lista[::2]) # começa em 0, vai até o final, de 2 em 2

# Invertendo valores em uma lista

nomes = ['Marcos', 'Silva']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes.reverse()
print(nomes)

# Soma, Valor Máximo, Valor Mínimo, Tamanho

# Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # máximo valor
print(min(lista)) # mínimo valor
print(len(lista)) # tamanho da lista

# Tranformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Obs: Se tivermos mais elementos para desempacotar do que variaveis para receber os valores, teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificamos uma lista, não afeta a outra, Isso em Python
# é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.
"""



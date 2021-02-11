"""
Módulo Collection - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Counter ({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# Veja que, para cada elemento da  lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Marcos Silva'))
# Counter({'a': 2, 'M': 1, 'r': 1, 'c': 1, 'o': 1, 's': 1, ' ': 1, 'S': 1, 'i': 1, 'l': 1, 'v': 1})

"""

# Utilizando o Counter

from collections import Counter

# Exemplo 3

texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting,
 remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 
 Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem 
 Ipsum."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))
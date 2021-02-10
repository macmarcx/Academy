"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

Histórico

nome = 'Marcos Silva'
print(nome)
print(type(nome))

nome = "Gina´s Bar"
print(nome)
print(type(nome))

nome = 'Marcos \nSilva'
print(nome)
print(type(nome))
"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# Deixa tudo maiúsculo
nome = 'Marcos Silva'
print(nome.upper())

# Deixa tudo minusculo
nome = 'Marcos Silva'
print(nome.lower())

# Cria uma lista de strings
nome = 'Marcos Silva'
print(nome.split())

"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Marcos Silva'
- Aspas duplas -> 'Marcos Silva'
- Aspas simples triplas -> '''Marcos Silva'''
"""
# Aspas duplas triplas -> """Marcos Silva"""

# Entrada de dados
# print("Qual seu nome? ")
# nome = input()
nome = input('Qual seu nome? ')

# Exemplo de print 'antigo' 2.x
# print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}' .format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print("Qual a sua idade? ")
# idade = input()

idade = input('Qual sua idade? ')

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print("O(a) %s tem %s anos" % (nome, idade))

# Exemplo de print 'mais atual' 3.x
# print('O(a) {0} tem {1} anos' .format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'O(a) {nome} tem {idade} anos')

"""
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'O(a) {nome} nasceu em {2021 - int(idade)} anos')

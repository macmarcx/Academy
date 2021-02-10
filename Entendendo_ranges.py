"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com o loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aletória,
mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Exemplo Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive(inicio especificado pelo usuário, e passo 1 em 1)

for num in range(1, 11):
    print(num)

# Exemplo forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive(início especificado pelo usuário, e passo especificoado pelo usuário)

for num in range(5, 50, 5):
    print(num)

# Exemplo Forma 4 (Inversa)

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive(valor_inicio especificado pelo usuário, e passo especificoado pelo usuário)
"""

for num in range(10, 0, -1):
    print(num)




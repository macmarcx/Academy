"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizamos a função integrada (Built-in) do Python print()

print(cores)
"""

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos: que é 
utilizado em Python para definir blocos.
"""

# Definindo a primeira função

def diz_oi():
    print('Oi!')

"""
OBS:

1 - Veja que, dentro das nossas funções podemos utilizar outras funções:
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Chamada de execução
diz_oi()

"""
ATENÇÂO:

Nunca esqueça de utilizar o parênteses ao executar uma função;

Exemplo:

# Errado!
diz_oi

# Certo!
diz_oi()

"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você ')
    print('Nesta data querida ')
    print('Muitas felicidades ')
    print('Muitos anos de vida ')
    print('Viva o aniversariante!')

#for n in range(5):
#    cantar_parabens()

canta = cantar_parabens()

canta
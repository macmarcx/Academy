"""
Documentando funções com Docstrings

OBS: Podemos ter acesso à documentação de uma função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso à documentação com a função help()
"""

# Exemplos

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'

print(diz_oi.__doc__)

def exponencial(numero, potencial=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencia' informada.
    :param numero: Número que desejamos gerar o exponecial.
    :param potencial: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potência'.
    """
    return numero ** potencia

print(exponencial.__doc__)
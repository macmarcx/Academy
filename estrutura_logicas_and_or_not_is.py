"""
Estruturas Lógicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or
"""
ativo = True
logado = False
name = "Marcos"

# Com Estrutura Lógica 'and'
if ativo and logado:
    print(f"Bem-vindo {name}")
else:
    print(f"Você precisa ativar sua conta. Por favor, cheque o seu e-mail {name}")

# Com Estrutura Lógica 'or'
if ativo or logado:
    print(f"Bem-vindo {name}")
else:
    print(f"Você precisa ativar sua conta. Por favor, cheque o seu e-mail {name}")

# Com Estrutura Lógica 'not'
if not logado:
    print(f"Bem-vindo {name}")
else:
    print(f"Você precisa ativar sua conta. Por favor, cheque o seu e-mail {name}")

# Com Estrutura Lógica 'is'
if ativo is logado:
    print(f"Bem-vindo {name}")
else:
    print(f"Você precisa ativar sua conta. Por favor, cheque o seu e-mail {name}")
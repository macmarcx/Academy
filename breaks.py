"""
Saindo de loops com break

Funciona da mesma forma que nas linguages C ou Java.

Utilizamos o break para sair de loops de maneira projetada.
"""

# Exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print(f"Sai do loop com {numero}")

# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
    elif comando != 'sair':
        print("Digite uma mensagem valida!")

print("Mensagem aceita, saindo do loop.")
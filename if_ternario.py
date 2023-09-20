# Permite escrever uma condição em uma única linha.
# Ele é composto por três partes, a primeira é o retorno caso a expressão retorne verdadeiro.
# A segunda parte é a expressão lógica e a terceira parte é o retorno caso expressão não seja atendida.

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
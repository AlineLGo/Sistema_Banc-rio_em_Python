# Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else
# dentro do bloco de código de estruturas if/elif/else

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 400
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso! ")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial! ")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente! ")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
# Banco deseja modernizar suas operações e para isso escolheu a linguagem python.
# implementar apenas 3 operações: deposito, saque e extrato

menu =  """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

 =>"""

saldo = 0
limite = 500
extrato = ""
quantidades_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou: Valor informado inválido. Tente novamente! ")
    elif opcao == "2":
        valor = float(input("Informe o valor saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = quantidades_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Operação Falhou. Saldo insuficiente! ")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            quantidades_saques += 1
            
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n=================== Extrato =======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")

    elif opcao == "4":
        break
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada")




# Operação de depósito
# Deve ser possivel depositar valores para a minha conta bancária. A v1 do proejto trabalha apenas com 1 usuario, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depositos devem ser armazenados em uma variavel e exibidos na operação de extrato

# Operação de saque
# Deve permitir realizar 3 saques diários com limite máximo de 500,00 por saque. Caso o usuario não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato

# Operação de extrato
# Deve listar todos os depositos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores deves ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45
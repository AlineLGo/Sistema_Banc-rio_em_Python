# While = é usado para repetir um bloco de código várias vezes. Faz sentido utilizar quando não
# sabemos o número extato de vezes que o bloco de cpodigo deve ser executado.

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    if opcao == 1:
        print("Sacando... ")
    elif opcao ==2:
        print("Exibindo o extrato... ")
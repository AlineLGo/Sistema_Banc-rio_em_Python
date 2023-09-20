# permitem o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas
# if = estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada
# if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no
# bloco de código do if serão executadas.

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque! ")
if saldo < saque:
    print("Saldo insuficiente!")

# if/else = para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else.
# Como sabemos se a expressão lógica testadas no if for verdadeira, então o bloco de código do if
# executado. Caso contrário o bloco de código do else será executado

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

# if/elif/else = mais de dois desvios, para isso podemos usar elif.
# O elif é composto por uma expressão lógica, que será testada e caso retorne verdadeiro o bloco de
#código do elif será executado.
# Não existe número máximo de elif, porém é melhor evitar criar grandes estruturas condicionais, pois,
# elas aumentam a complexidade do código

opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato:"))

if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")
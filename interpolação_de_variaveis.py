# Old style % = muito raro ser utilizado no python

nome = "Aline"
idade = 28
profissao = "Assistente"
linguagem = "Python"

print("Olá, me chamo %s. Tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))
 
 # Metodo format
print("Olá, me chamo {3} Tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

# Metodo f-string
print(f"Olá, me chamo {nome} Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# formatar strings com f-string
PI = 3.14159
print(f"Valor de PI:{PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")

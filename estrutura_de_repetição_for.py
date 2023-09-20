# São utilizadas para repetir um trecho de código um determinado número de vezes.
# Esse número pode ser conhecido previamente ou determinado atrvés de uma expressão lógica.

# for = percorre um objeto iterável. Faz sentido utilizar quando se sabe o número exato de vezes que 
# o bloco de código deve ser executado, ou quando se quer percorrer um objeto iterável.

texto = input("Informe um texto: ")
VOGAIS = " AEIOU"

for letra in texto:
    if letra.upper() in  VOGAIS:
        print(letra, end="")
print()

# Função range = função built-in do Python, é usada para produzir uma sequência de números inteiros 
# a partir de um ínicio (inclusivo) para um fim (exclusivo). Se usarmos range (i,j)
# será produzido: i, i+1, i+2, i+3,..., j-1.
# Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional)
for numero in range (0,11):
    print(numero, end="\n")

for numero in range(0,51,5):
    print(numero, end=" ") # tabuada do 5




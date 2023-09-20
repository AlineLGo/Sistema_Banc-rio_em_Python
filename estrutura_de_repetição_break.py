#while True:
    #numero = int(input("Informe um número: "))
    #if numero == 10:
       # break
#print(numero)
# quando chega na determinada condição o programa para de rodar o código

for numero in range(100):
    if numero == 12:
        continue
print(numero, end="")
# utilizado quando se quer pular uma situação especifica

curso = "Python"                                                     
print(curso[::-1])    
import random

numero = random.randint(1, 10)
opcion = int(input("Adivina el numero de 1 a 10: "))

if numero == opcion:
    print("Enhorabuena, has acertado")

print("El numero ganador es: {}".format(numero))

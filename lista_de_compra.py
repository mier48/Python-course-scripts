print("***LISTA DE LA COMRPA***")

lista_compra = []

val = input("¿Que deseas comprar? ([Q] para salir)\n")
while val != "Q" and val != "q":
    print("Has añadido {} a la lista\n".format(val))
    lista_compra.append(val)
    val = input("¿Que deseas comprar? ([Q] para salir)\n")

print("\nLa lista de la compra es: ")
print(lista_compra)

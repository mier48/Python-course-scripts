edad = int(input("Cual es tu edad?: "))
carnet = input("Cual es tu carnet? E, P, FN, N: ")

if (25 <= edad <= 35 and carnet == "E") or (edad <= 10) or (edad > 65 and carnet == "P") or carnet == "FN":
    print("Se le aplica el descuento")
else:
    print("No se te aplica el descuento")

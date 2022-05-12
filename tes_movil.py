print("Bienvenido\n**********\n")
opcion = input("Pregunta 1: ¿Android o IOS?\n")

if opcion == "android":
    opcion = input("Pregunta 2: ¿Tienes dinero?\n")
    if opcion == "no":
        print("Android chino de 100€")
    elif opcion == "si":
        opcion = input("Pregunta 3: ¿Te importa la camara del movil?")
        if opcion == "si":
            print("Google pixel con supercamara")
        elif opcion == "no":
            print("Android calidad-precio")
elif opcion == "ios":
    opcion = input("Pregunta 2: ¿Tienes dinero?\n")
    if opcion == "no":
        print("Iphone segunda mano")
    elif opcion == "si":
        print("Iphone 13 ultra coral level cancun pro max")

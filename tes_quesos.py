total_score = 0

txt = "Bienvenido al test sobre el queso"
print("\n" + txt + "\n" + "*" * len(txt) +"\n")

opcion = input("""Pregunta 1: ¿Que haces cuando ves una tabla de quesos?
A- Salgo corriendo
B- Pruebo uno de los quesos, o incluso varios
C- No puedo evitar devorarla\n""")

if opcion == "A":
    pass
elif opcion == "B":
    total_score += 5
elif opcion == "C":
    total_score  += 10
else:
    print("Las opciones posibles son A, B, C")
    exit()

opcion = input("""Pregunta 2: ¿Como te gusta la hambueguesa?
A- Sin queso
B- Con queso
C- Pan y queso\n""")

if opcion == "A":
    pass
elif opcion == "B":
    total_score += 5
elif opcion == "C":
    total_score  += 10
else:
    print("Las opciones posibles son A, B, C")
    exit()

opcion = input("""Pregunta 3: ¿Eres intolerante a la lactosa?
A- Si
B- A veces
C- No\n""")

if opcion == "A":
    pass
elif opcion == "B":
    total_score += 5
elif opcion == "C":
    total_score  += 10
else:
    print("Las opciones posibles son A, B, C")
    exit()

if total_score < 10:
    print("No te gusta el queso")
elif total_score <= 20:
    print("Te gusta el queso")
elif 20 < total_score <= 30:
    print("Te encanta el queso")

exit()

print("La puntuación es: {}".format(total_score))

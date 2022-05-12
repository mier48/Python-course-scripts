print("Voy a la cocina")
print("abro la nevera")

hay_leche = (input("Hay leche? (S/N)"))
hay_colacao = input("Hay colacao? (S/N)")

if hay_leche != "S" or hay_colacao != "S":
    print("Voy al super")
    if hay_leche != "S":
        print("Comprar leche")
    if hay_colacao != "S":
        print("Comprar colacao")

print("Sacamos la leche de la nevera")
print("Sacar el colacao")
print("Mezclarlo")

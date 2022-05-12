from random import randint


VIDA_INICIAL_PIKACHU = 100
VIDA_INICIAL_SQUIRTLE = 100

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    #combate

    print("**turno de pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #rayo
        print("pikachu ataca con rayo")
        vida_squirtle -= 20
    elif ataque_pikachu == 2:
        print("pikachu ataca con placaje")
        vida_squirtle -= 10

    if vida_squirtle < 0:
        vida_squirtle = 0

    print("Vida squirtle = {}".format(vida_squirtle))

    barras_de_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle: [{}{}]".format("*" * barras_de_vida_squirtle, " " * (10 - barras_de_vida_squirtle)))

    print("**turno de squirtle")
    ataque = input("Que ataque deseas realizar? Placaje [P], Pistola agua [A]\n")
    while ataque != "P" and ataque != "A":
        ataque = input("Que ataque deseas realizar? Placaje [P], Pistola agua [A]\n")

    if ataque == "P":
        vida_pikachu -= 10
    elif ataque == "A":
        vida_pikachu -= 15

    if vida_pikachu < 0:
        vida_pikachu = 0


    print("Vida pikachu = {}".format(vida_pikachu))

    barras_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
    print("Pikachu: [{}{}]".format("*" * barras_de_vida_pikachu, " " * (10 - barras_de_vida_pikachu)))
    print("***************************************")


if vida_pikachu > vida_squirtle:
    print("gana pikachu")
else:
    print("Gana squirtle")

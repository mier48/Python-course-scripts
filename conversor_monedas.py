
dolar_euro = 0.9
libra_euro = 1.19
euro_dolar = 1.11
euro_libra = 0.84
opcion = input("""¿Que divisa quieres cambiar?
A- Euro a dolar
B- Dolar a euro
C- Euro a libras
D- Libra a euro\n""")

cantidad = int(input("Introduce la cantidad: \n"))

if opcion == "A":
    euros = cantidad * euro_dolar
    print("{}€ son: {} dolares".format(cantidad, euros))
elif opcion == "B":
    dolares = cantidad * dolar_euro
    print("{}$ son: {} euros".format(cantidad, dolares))
elif opcion == "C":
    euros = cantidad * euro_libra
    print("{}€ son: {} libras".format(cantidad, euros))
elif opcion == "D":
    libras = cantidad * libra_euro
    print("{}L son: {} euros".format(cantidad, libras))

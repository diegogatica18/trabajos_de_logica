cartel = input("Introduzca un texto:")
largo = len(cartel)
maslinea = ("+---")
print(maslinea * len(cartel)+ "+")
print("| ", end="")
for letras in (cartel):
    print(letras, end=" | ")
    print(end="")
print()
print(maslinea * len(cartel)+ "+")



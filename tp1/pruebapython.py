import os 
os.system("clear")
cartel = input("Introduzca un texto: ").upper().strip(" ")
import os 
def limpiar_pantalla():
	print("\n" * 200)
while True:
	medio = ""
	if cartel:
		print("┏" + "━━━━━" * len(cartel) + "┓")
		for letra in cartel:
			medio += "  " + letra + "  "
		print('┃' + medio + '┃')	
		print("┗" + "━━━━━" * len(cartel) + "┛")
		presionar_enter = input ("pulse <enter> para retornar:")
		limpiar_pantalla, print("\n" * 200)
		cartel = input("pulsar enter para salir o ingresar un nuevo texto: ").strip(" ")
	else:
		cartel == "" 
		print ("salida exitosa")
		break
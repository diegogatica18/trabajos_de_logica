def crear_lista():
    palabras = []
    while True:
        palabra = input("Ingrese una palabra, haga espacio e ingrese la siguiente y al terminar presione <enter>")
        palabra = palabra.split(" ")
        if palabra == " ":
            break
    
        palabras.append(palabra)
        return palabras
    lista_palabras = crear_lista()
    print("Lista de palabras:")
    for palabra in lista_palabras:
        print(lista_palabras)
    

def crear_suma_de_flotantes():
    entrada = input("Ingrese un número: ")
    return entrada
       
def crear_suma_de_enteros():
    entrada = input("Ingrese un número:" )
    return entrada
def crear_un_diccionario():
    diccionario = {}
    return diccionario

def pedir_fecha():
    dia = input("Por favor, ingresa el día (en letras, por ejemplo 'lunes'): ").strip().upper()
    while True:
        try:
            numero_del_dia = int(input("Ingresar el numero del dia (en numero, por ejemplo '10'): ").strip())
            break
        except ValueError:
            print("Formato no valido")      
    mes = input("Por favor, ingresa el mes (en letras, por ejemplo 'mayo'): ").strip().upper()
    while True:
        try:
            año = int(input("Por favor, ingresa el año (en números, por ejemplo '2024'): ").strip())
            break
        except:
            print("Formato no valido")
    fecha_formateada = f"{dia} {numero_del_dia} de {mes} de {año}"
    print("resultado de la fecha ingresada")
    print(fecha_formateada)

def obtener_informacion():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except:
            print("Error formato no valido")
    return nombre, apellido, edad

def menu():
    print("1. Sumar enteros")
    print("2. Sumar flotantes")
    print("3. Pedir fecha")
    print("4. Obtener información del usuario")
    print("5. Diccionario")
    print("6. arma tu lista")
    print("7. Salir")


diccionario = {}

while True:
    menu()
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        try:
            resultado = int(crear_suma_de_enteros()) + int(crear_suma_de_enteros())
            print()
            print("El resultado de la suma de enteros es:", resultado)
        except:
            print("Error! formato no valido")
    elif opcion == "2":
        try:
            resultado = float(crear_suma_de_flotantes()) + float(crear_suma_de_flotantes())
            print("El resultado de la suma de flotantes es:", resultado)
        except:
            print("Error! formato no valido")
    
    elif opcion == "3":
        pedir_fecha()
    elif opcion == "4":
        informacion_usuario = obtener_informacion()
        print("\nInformación del usuario:", informacion_usuario)
    elif opcion=="5":
        la_palabra = input(f"Ingrese la palabra: ")
        definicion = input(f"Ingrese la definición de '{la_palabra}': ")
        diccionario[la_palabra] = definicion
        print("\nDiccionario creado:")
        for clave, definicion in diccionario.items():
            print(f"{la_palabra}: {definicion}")
    elif opcion == "6":
        print("Ingrese todas las palabras separada solo con espacios: ")
        lista_palabras = crear_lista()
        print("Lista de palabras:")
        for palabra in lista_palabras:
            print(palabra)
        elementos = len(palabra)
        print ("la lista contiene", elementos, "elementos")
    elif opcion == "7":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
    print()
    input("desea volver al inicio <ENTER>" )
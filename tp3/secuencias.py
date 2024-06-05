def ingresar_dato(mensaje):
    """premite el ingreso de un dato yvalida que sea numerico"""
    while True:
        numero = input(mensaje)
        try:
            numero = int(numero)
            break
            
        except:
            print ("tipo de dato incorrecto")
            continue
    return(numero)
def mostrar_secuencia(s):
    for iterador in secuencia:
        print(iterador)
        return

#cuerpo principal del programa
valor_inicial = ingresar_dato("ingresar el valor numerico inicial: ")
valor_final = ingresar_dato("ingrese el valor numerico final: ")
salto = ingresar_dato("ingresae el salto: ")
secuencia = range(valor_inicial, valor_final, salto)
mostrar_secuencia(secuencia)
archivo = open("secuencia.txt", "w")
for
archivo.write(secuencia)
archivo.close()

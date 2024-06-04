# Series de Fibonacci: la suma de dos elementos define el siguiente
from os import system

def borrar_pantalla():
    '''Limpia la terminal pero solo en distros linux.'''
    system('clear')

def ingresar_tope():
    '''Solicita al operador un valor de tope para la serie de fibonacci.'''
    numero = input('Ingrese un valor numérico límite (0 para terminar): ')
    try:
        numero = int(numero)
        return numero
    except:
        print('Debe ingresar un valor numérico entero!')
        pausar('')
        return 0

def fibonacci(limite): 
    '''Devuelve una lista conteniendo la serie de Fibonacci hasta cierto límite.'''
    suc = []
    a, b = 0, 1
    while a < limite:
        suc.append(a)
        a, b = b, a + b
    return suc

def mostrar_serie(sf):
    '''Muestra la serie de una forma decorosa.'''
    cantidad = len(sf)
    for item in sf:
        print(item, end=' ')
    print('\nEsta serie contiene', cantidad, 'elementos')

def pausar(mensaje):
    '''Solo una simple pausa.'''
    print()
    nada = input(mensaje)
    return
    
#cuerpo principal del programa
ejecuciones = 0
while True:
    borrar_pantalla()
    limite = ingresar_tope()
    if not limite:
        break
    sucesion = fibonacci(limite)
    mostrar_serie(sucesion)
    ejecuciones += 1
    pausar('Pulse <ENTER> para otra serie.')

borrar_pantalla()
print('Ud ha solicitado', ejecuciones, 'sucesiones de Fibonacci, gracias por utilizar este programa.')
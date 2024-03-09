from usuariodao import *

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. SELECCIONAR')
        print('2. INSETAR')
        print('3. ACTUALIZAR')
        print('4. ELIMINAR')
        opcion = int(input('Escribe tu Opcion (1-4) :'))

        if opcion == 1:
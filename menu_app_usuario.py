from conexion import Conexion
from usuariodao import *

opcion = None
while opcion != 5:
    try:
        print('Opciones: ')
        print('1. SELECCIONAR')
        print('2. INSETAR')
        print('3. ACTUALIZAR')
        print('4. ELIMINAR')
        print('5. EXIT')

        opcion = int(input('Escribe tu Opcion (1-4) :'))

        if opcion == 1:
            usur1 = UsuarioDao.seleccionar()
            for usuario in usur1:
                print(usur1)

        elif opcion == 2:
            usuario = input('Dijite el usuario: ')
            password = input('Digite la contraseña: ')
            user1 = Usuario(username=usuario, password=password)
            userin = UsuarioDao.insertar(user1)
            log.debug(f'Personas insertadas: {userin}')

        elif opcion == 3:
            id = input('Digite el Id le usuario para actuualizar: ')
            usuario = input('Dijite el usuario: ')
            password = input('Digite la contraseña: ')
            user1 = Usuario(id, usuario, password)
            userin = UsuarioDao.actualizar(user1)
            log.debug(f'Personas actualizadas: {userin}')

        elif opcion == 4:
            id = input('Dijite el Id del usuario a eliminar: ')
            user1 = Usuario(id_user=id)
            userin = UsuarioDao.eliminar(user1)
            log.debug(f'Personas eliminadas: {userin}')

    except Exception as a:
        print(f'ocurrio un error {a}')
        opcion = None
else:
    print('Salimos del programa'.center(50, '#'))


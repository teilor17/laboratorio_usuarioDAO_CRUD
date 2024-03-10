from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import log
class UsuarioDao:
    _SELECCIONAR = 'SELECT * FROM usuarios'
    _INSERTAR = 'INSERT INTO usuarios (username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                user = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(user)
                print(f'Registros: {user}')
            return cursor
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_user)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_user,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Persona eliminada: {usuario}')
            return cursor.rowcount


if __name__ == '__main__':


    '''user1 = Usuario(username='Hielo', password='548545')
    userin = UsuarioDao.insertar(user1)
    log.debug(f'Personas insertadas: {userin}')'''

    # Actualizar un registro
    '''user1 = Usuario(2, 'tatiana', '54321')
    userin = UsuarioDao.actualizar(user1)
    log.debug(f'Personas actualizadas: {userin}')'''

    # Eliminar un registro
    '''user1 = Usuario(id_user=3)
    userin = UsuarioDao.eliminar(user1)
    log.debug(f'Personas eliminadas: {userin}')'''
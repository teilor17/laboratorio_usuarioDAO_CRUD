from conexion import *
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        log.debug('__ENTER__')
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('__EXIT__')
        if exc_val:
            self._conn.rollback()
            log.error(f'EROOR __EXIT__ : {exc_val} {exc_type} {exc_tb}')
        else:
            self._conn.commit()
            log.debug('COMMIT')
        self._cursor.close()
        Conexion.liberarConexion(self._conn)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM personas')
        log.debug(cursor.fetchall())

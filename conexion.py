import sys
from logger_base import log
from psycopg2 import pool

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = '127.0.0.1'
    _PORT = '5432'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._PORT,
                                                      database=cls._DATABASE)
                log.debug(f'CONECTADO (ObtenerPool): {cls._pool}')
                return cls._pool

            except Exception as e:
                log.error(f'ERROR (obtenerPool): {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = Conexion.obtenerPool().getconn()
        log.debug(f'CONEXION CORRECTA: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        Conexion.obtenerPool().putconn(conexion)
        log.debug(f'CONEXION CERRADA: {conexion}')

    @classmethod
    def CerrarConexiones(cls):
        Conexion.obtenerPool().closeall()
        log.debug('CONEXIONES CERRADAS')


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    Conexion.CerrarConexiones()

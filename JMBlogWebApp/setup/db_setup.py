import setup.postgres_scripts as scripts
from setup.db_connect import DbConnect
from setup.config import Config

class DbSetup():
    def __init__(self):
        self._config = None

    def create_database(self):
        self._config = Config().from_file('db_connection')
        conn = DbConnect(hasDb=False)
        conn.get_parameters(**self._config)
        conn.create_connection()

        if not conn.contains_database(self._config.get('database')):

            conn.execute(scripts.CREATE_DATABASE_SCRIPT % self._config['database'])
            conn.close_connection()

            conn = DbConnect()
            conn.get_parameters(**self._config)
            conn.create_connection()

            conn.execute(scripts.CREATE_TABLE_SCRIPT)
            conn.close_connection()

        conn = DbConnect()
        conn.get_parameters(**self._config)
        conn.create_connection()

        if not conn.contains_table():
            conn.execute(scripts.CREATE_TABLE_SCRIPT)

        conn.close_connection()


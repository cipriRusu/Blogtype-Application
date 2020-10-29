import setup.postgres_scripts as scripts
from setup.db_connect import DbConnect

class DbSetup():
    def __init__(self, db_config):
        self._config = db_config

    def create_database(self):
        conn = DbConnect(self._config, hasDb=False)
        conn.create_connection()

        if not conn.contains_database(self._config.from_file('db_connection').get('database')):

            conn.execute(scripts.CREATE_DATABASE_SCRIPT % self._config.from_file['database'])
            conn.close_connection()

            conn = DbConnect(self._config)
            conn.create_connection()

            conn.execute(scripts.CREATE_TABLE_SCRIPT)
            conn.close_connection()

        conn = DbConnect(self._config)
        conn.create_connection()

        if not conn.contains_table():
            conn.execute(scripts.CREATE_TABLE_SCRIPT)

        conn.close_connection()

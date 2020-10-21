import setup.postgres_scripts as scripts
from setup.db_connect import DbConnect

class DbSetup():
    def __init__(self, **connection_params):
        self._params = connection_params
        self._connection = self.create_database()

    def create_database(self):

        conn = DbConnect(hasDb=False, **self._params)

        if not conn.contains_database(self._params.get('database')):

            conn.execute(scripts.CREATE_DATABASE_SCRIPT % self._params['database'])

            conn = DbConnect(**self._params)

            conn.execute(scripts.CREATE_TABLE_SCRIPT)

        conn = DbConnect(**self._params)

        if not conn.contains_table():
            conn.execute(scripts.CREATE_TABLE_SCRIPT)

        return conn

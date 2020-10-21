import psycopg2
import setup.postgres_scripts as scripts
from setup.db_connect import DbConnect

class DbSetup():
    def __init__(self, connection_params):
        self._params = connection_params
        self._connection = self.create_database()
        self._cursor = self._connection.cursor()

    def execute_query(self, query, args=None):
        if args is None:
            self._cursor.execute(query)
        else:
            self._cursor.execute(query, args)
        return self._cursor

    def create_database(self):

        conn = DbConnect(hasDb=False, **self._params)

        if not conn.contains_database(self._params.get('database')):

            conn.execute(scripts.CREATE_DATABASE_SCRIPT % self._params['database'])

            conn = DbConnect(**self._params)

            conn.execute(scripts.CREATE_TABLE_SCRIPT)

        conn = DbConnect(**self._params)

        if not conn.contains_table():
            conn.execute(scripts.CREATE_TABLE_SCRIPT)

        return psycopg2.connect(**self._params)

    def close_connection(self):
        self._cursor.close()
        self._connection.commit()
        self._connection.close()

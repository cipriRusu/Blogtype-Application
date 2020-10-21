import psycopg2
import setup.postgres_scripts as scripts

class DbConnect():
    def __init__(self, hasDb=True, **params):
        if hasDb:
            self._params = params
        else:
            self._params = params
            del self._params['database']

        self._connection = psycopg2.connect(**self._params)
        self._connection.autocommit = True
        self._cursor = self._connection.cursor()

    def execute(self, query, args=None):
        if args is None:
            self._cursor.execute(query)
        else:
            self._cursor.execute(query, args)
        return self._cursor

    def contains_database(self, db_name):
        self._cursor.execute(scripts.LIST_DATABASES_SCRIPT)
        contained = self._cursor.fetchall()
        databases = [x[0] for x in contained]
        return db_name in databases

    def contains_table(self):
        self._cursor.execute(scripts.SEARCH_TABLE_SCRIPT % ("'posts'",))
        return self._cursor.fetchone()[0]

    def close_connection(self):
        self._cursor.close()
        self._connection.commit()
        self._connection.close()

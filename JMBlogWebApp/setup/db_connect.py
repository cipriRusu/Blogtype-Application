import psycopg2
import setup.postgres_scripts as scripts

class DbConnect():
    def __init__(self, config):
        self._config = config
        self._connection = None
        self._cursor = None

    def create_connection(self):
        self._connection = psycopg2.connect(**self._config.from_file('db_connection'))
        self._connection.autocommit = True
        self._cursor = self._connection.cursor()

    def contains_table(self):
        self._cursor.execute(scripts.SEARCH_TABLE_SCRIPT % ("'posts'",))
        return self._cursor.fetchone()[0]

    def close_connection(self):
        self._cursor.close()
        self._connection.commit()
        self._connection.close()

    def execute(self, query, args=None):
        if args is None:
            self._cursor.execute(query)
        else:
            self._cursor.execute(query, args)
        return self._cursor

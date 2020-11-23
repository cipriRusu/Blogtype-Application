import psycopg2
import setup.postgres_scripts as scripts

class DbConnect():
    def __init__(self, config):
        self._config = config
        self._loaded_config = None
        self._connection = None
        self._cursor = None

    def create_connection(self):
        self._loaded_config = self._config.load_configuration()
        self._connection = psycopg2.connect(**self._loaded_config.get_dictionary())
        self._connection.autocommit = True
        self._cursor = self._connection.cursor()

    def create_db(self):
        self._connection = psycopg2.connect('host=localhost user=postgres password=testpass')
        self._connection.autocommit = True
        self._cursor = self._connection.cursor()
        self._cursor.execute('''CREATE DATABASE posts''')
        self._cursor.close()
        self._connection.close()

    def update_database(self):
        pass

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

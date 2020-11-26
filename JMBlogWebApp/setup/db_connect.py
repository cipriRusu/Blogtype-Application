import psycopg2
import setup.postgres_scripts as scripts
from models.database_version import DatabaseVersion

class DbConnect():
    CONNECTION_STRING = 'host=localhost user=postgres password=testpass'

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
        self._connection = psycopg2.connect(DbConnect.CONNECTION_STRING)
        self._connection.autocommit = True
        self._cursor = self._connection.cursor()
        self._cursor.execute(scripts.CREATE_DATABASE_SCRIPT.format('posts'))
        self._cursor.close()
        self._connection.close()
        self._config.set_db_version(DatabaseVersion(3))

    def can_update(self):
        return self._config.get_db_version() != 3

    def update_db(self):
        if self._config.is_configured():
            self.create_connection()
            for script in scripts.UPDATE_EXISTING_DB:
                self.execute(script)
            self._config.set_db_version(DatabaseVersion(3))

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

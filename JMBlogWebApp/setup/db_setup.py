import psycopg2
import setup.postgres_scripts as scripts
from models.database_version import DatabaseVersion

class DbSetup():
    LATEST_VERSION = 3

    def __init__(self, db_connection):
        self._connection = db_connection
        self._configuration = db_connection._config
        self._db_version = 0
        self._params = None

    def create_db(self):
        _params = self._configuration.load_configuration().get_dictionary()
        _conn = psycopg2.connect(**{x: _params[x] for x in ['host', 'user', 'password']})
        _conn.autocommit = True
        _cursor = _conn.cursor()
        _cursor.execute('''CREATE DATABASE {}'''.format(_params['database']))
        _cursor.close()
        _conn.close()

    def update_db(self):
        if self._configuration.is_configured():
            if self._configuration.get_db_version() != DbSetup.LATEST_VERSION:
                self._connection.create_connection()
                for script in scripts.ALL_SCRIPTS:
                    self._connection.execute(script)
                self._connection.close_connection()
        self._configuration.set_db_version(DatabaseVersion(3))

    def setup(self):
        try:
            self.create_db()
        except psycopg2.DatabaseError:
            pass
        self.update_db()

    def is_db_outdated(self):
        return (self._configuration.is_configured() and
                self._configuration.get_db_version() != DbSetup.LATEST_VERSION)

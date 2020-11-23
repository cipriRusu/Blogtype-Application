from models.database_version import DatabaseVersion
import setup.postgres_scripts as scripts

class DbSetup():
    def __init__(self, db_connection):
        self._connection = db_connection
        self._configuration = db_connection._config
        self._db_version = 0

    def create_db(self):
        try:
            self._connection.create_connection()
        except:
            raise Exception(self._connection,
                            "Connection cannot be established\
                             as there is no local available database")

        if not self._connection.contains_table():
            for script in scripts.CREATE_FULL_DATABASE:
                self._connection.execute(script)

        self._connection.close_connection()

    def update_database(self):
        try:
            self._connection.create_connection()
            ##TODO:UPDATE IF NEEDED##
            self._connection.close_connection()
        except:
            ##TODO:CREATE DB FROM SCRATCH##
            pass

        self._configuration.set_db_version(DatabaseVersion(3))

    def is_db_outdated(self):
        return self._configuration.get_db_version() != 3

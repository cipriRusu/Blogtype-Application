import setup.postgres_scripts as scripts

class DbSetup():
    LATEST_VERSION = 3
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

        if self._connection.can_update():
            self.update_database()

        for script in scripts.CREATE_ALL_DB_RELATIONS:
            self._connection.execute(script)

        self._connection.close_connection()

    def update_database(self):
        try:
            self._connection.create_db()
        except:
            self._connection.update_db()

    def is_db_outdated(self):
        return self._configuration.get_db_version() != DbSetup.LATEST_VERSION

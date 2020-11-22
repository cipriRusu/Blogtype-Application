import setup.postgres_scripts as scripts

class DbSetup():
    def __init__(self, db_connection):
        self._connection = db_connection
        self._db_version = 0

    def create_db(self):
        try:
            self._connection.create_connection()
        except:
            raise Exception(self._connection,
                            "Connection cannot be established\
                             as there is no local available database")

        self._connection.close_connection()

    def update_database(self):
        self._connection.create_connection()
        for script in scripts.CREATE_FULL_DATABASE:
            self._connection.execute(script)
        self._connection.close_connection()

    def is_db_outdated(self):
        pass
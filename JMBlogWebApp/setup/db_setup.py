import setup.postgres_scripts as scripts

class DbSetup():
    def __init__(self, db_connection):
        self._connection = db_connection

    def create_database(self):
        try:
            self._connection.create_connection()
        except:
            raise Exception(self._connection,
                            "Connection cannot be established\
                             as there is no local available database")

        if not self._connection.contains_table():
            self._connection.execute(scripts.CREATE_TABLE_SCRIPT)

        self._connection.close_connection()

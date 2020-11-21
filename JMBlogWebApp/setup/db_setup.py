from setup.config import Config
import setup.postgres_scripts as scripts

class DbSetup():
    def __init__(self, db_connection):
        self._connection = db_connection
        self._db_version = 0

    def establish_connection(self):
        try:
            self._connection.create_connection()
        except:
            raise Exception(self._connection,
                            "Connection cannot be established\
                             as there is no local available database")

        self._connection.close_connection()

    def update_database(self):
        current_configuration = Config().from_file('db_connection')

        if self._db_version == 0:
            self._connection.create_host_connection()

            if not self._connection.contains_db(current_configuration['database']):
                self._connection.execute(scripts.CREATE_DATABASE_SCRIPT %
                                         current_configuration['database'])
                self._connection.close_connection()

                self._connection.create_connection()
                self._connection.execute(scripts.CREATE_USERS_SCRIPT)
                self._connection.execute(scripts.CREATE_POSTS_SCRIPT)
                self._connection.execute(scripts.CREATE_ADMIN_SCRIPT)
                self._connection.close_connection()

    def set_version(self):
        if Config().is_configured():
            if Config().has_section('db_version'):
                self._db_version = int(Config().from_file('db_version')['version'])

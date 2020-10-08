from configparser import ConfigParser
import psycopg2

CONFIG_PATH = 'setup/database.ini'
CONFIG_HEADER = 'postgresql_conn_data'

class DBConnectionSetup():
    def __init__(self):
        self.config_parser = ConfigParser()

    def get_connection(self):
        self.config_parser.read(CONFIG_PATH)
        config_params = self.config_parser.items(CONFIG_HEADER)
        db_conn_dict = {}

        for config_param in config_params:
            key = config_param[0]
            value = config_param[1]
            db_conn_dict[key] = value

        conn = psycopg2.connect(**db_conn_dict)
        return conn

    def close_connection(self, connection, cursor):
        connection.commit()
        cursor.close()
        connection.close()

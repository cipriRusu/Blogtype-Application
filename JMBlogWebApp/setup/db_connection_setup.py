from configparser import ConfigParser
import psycopg2

CONFIG_PATH = 'setup/config.ini'
CONFIG_HEADER = 'postgresql_conn_data'

class DBConnectionSetup():
    def __init__(self):
        self.config_parser = ConfigParser()
        self.connection = self.__get_connection()
        self.cursor = self.connection.cursor()

    def execute_query(self, query, args=None):
        if args is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, args)
        return self.cursor

    def close_connection(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

    def __get_connection(self):
        self.config_parser.read(CONFIG_PATH)
        config_params = self.config_parser.items(CONFIG_HEADER)
        db_conn_dict = {}

        for config_param in config_params:
            key = config_param[0]
            value = config_param[1]
            db_conn_dict[key] = value

        conn = psycopg2.connect(**db_conn_dict)
        return conn

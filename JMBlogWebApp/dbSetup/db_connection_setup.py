from configparser import ConfigParser
import psycopg2

class DBConnectionSetup():
    def __init__(self):
        self.config_parser = ConfigParser()

    def get_connection(self, file_path, file_section):
        self.config_parser.read(file_path)
        config_params = self.config_parser.items(file_section)
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

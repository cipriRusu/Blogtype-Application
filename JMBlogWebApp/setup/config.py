from os import path
from configparser import ConfigParser

CONFIG_PATH = 'setup/config.ini'

class Config():
    def __init__(self):
        self._config_path = CONFIG_PATH
        self._config_parser = ConfigParser()

    def from_file(self, header):
        self.read_file()
        config_params = self._config_parser.items(header)
        db_conn_dict = {}

        for config_param in config_params:
            key = config_param[0]
            value = config_param[1]
            db_conn_dict[key] = value

        return db_conn_dict

    def read_file(self):
        self._config_parser.read(self._config_path)

    def to_file(self, source, header):
        self._config_parser[header] = source
        with open(self._config_path, 'w+') as configfile:
            self._config_parser.write(configfile)

    def has_section(self, header):
        self.read_file()
        return self._config_parser.has_section(header)

    @classmethod
    def is_configured(cls):
        if path.exists(CONFIG_PATH):
            return True
        return False

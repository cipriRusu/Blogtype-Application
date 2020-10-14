from configparser import ConfigParser

CONFIG_PATH = 'setup/config.ini'

class Config():
    def __init__(self):
        self._config_parser = ConfigParser()

    def from_file(self, header):
        self._config_parser.read(CONFIG_PATH)
        config_params = self._config_parser.items(header)
        db_conn_dict = {}

        for config_param in config_params:
            key = config_param[0]
            value = config_param[1]
            db_conn_dict[key] = value

        return db_conn_dict

    def to_file(self, source, header):
        self._config_parser[header] = source
        with open('./setup/config.ini', 'w+') as configfile:
            self._config_parser.write(configfile)

from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class SQAEngine():
    DB_ENGINE = 'postgres+psycopg2'
    def __init__(self, config):
        self._config = config
        self._loaded_config = None
        self._current_engine = None
        self._current_session = None

    def start_session(self):
        engine_config_dictionary = self._get_conn_dictionary()
        url = URL(**engine_config_dictionary)
        self._current_engine = create_engine(url)

    def get_session(self):
        session = sessionmaker(bind=self._current_engine)
        self._current_session = session()
        return self._current_session

    def close_session(self):
        #False positive?
        self._current_session.commit()
        self._current_session.close()

    def _get_conn_dictionary(self):
        self._loaded_config = self._config.load_configuration().get_dictionary()

        return dict(drivername=SQAEngine.DB_ENGINE,
                    username=self._loaded_config['user'],
                    password=self._loaded_config['password'],
                    host=self._loaded_config['host'],
                    port=self._loaded_config['port'],
                    database=self._loaded_config['database'])

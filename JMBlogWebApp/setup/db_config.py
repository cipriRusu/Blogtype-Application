from models.database_configuration import DatabaseConfiguration
from setup.config import Config

class DbConfig(Config):
    DB_CONNECTION_HEADER = 'db_connection'

    def load_configuration(self):
        return DatabaseConfiguration(**super().from_file(DbConfig.DB_CONNECTION_HEADER))

    def save_configuration(self, received_stats):
        super().to_file(received_stats, DbConfig.DB_CONNECTION_HEADER)

    def is_configured(self):
        return super().is_configured() and super().has_section(DbConfig.DB_CONNECTION_HEADER)

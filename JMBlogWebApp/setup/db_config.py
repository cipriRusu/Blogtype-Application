from models.database_configuration import DatabaseConfiguration
from setup.config import Config
from setup.db_default import DefaultConfiguration

class DbConfig(Config):
    DB_CONNECTION_HEADER = 'db_connection'
    DB_VERSION_HEADER = 'db_version'

    def load_configuration(self):
        if self.is_configured():
            return DatabaseConfiguration(**super().from_file(DbConfig.DB_CONNECTION_HEADER))
        return DefaultConfiguration()

    def save_configuration(self, received_stats):
        super().to_file(received_stats, DbConfig.DB_CONNECTION_HEADER)

    def is_configured(self):
        return super().is_configured() and super().has_section(DbConfig.DB_CONNECTION_HEADER)

    def get_db_version(self):
        if super().is_configured() and super().has_section(DbConfig.DB_VERSION_HEADER):
            return super().from_file(DbConfig.DB_VERSION_HEADER)
        return 0

    def set_db_version(self, updated_version):
        super().to_file(updated_version, DbConfig.DB_VERSION_HEADER)

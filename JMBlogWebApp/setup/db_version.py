from setup.config import Config

class DbVersion(Config):
    DB_CONNECTION_HEADER = 'db_version'

    def load_configuration(self):
        return super().from_file(DbVersion.DB_CONNECTION_HEADER)

    def save_configuration(self, received_stats):
        super().to_file(received_stats, DbVersion.DB_CONNECTION_HEADER)

    def is_configured(self):
        return super().is_configured() and super().has_section(DbVersion.DB_CONNECTION_HEADER)

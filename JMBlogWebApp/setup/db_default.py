from models.database_configuration import DatabaseConfiguration

class DefaultConfiguration(DatabaseConfiguration):
    def __init__(self):
        self.host = 'localhost'
        self.port = 5432
        self.user = 'postgres'
        self.password = 'testpass'

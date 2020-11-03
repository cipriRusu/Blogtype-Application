class DatabaseConfiguration:
    def __init__(self, database, port, user, password):
        self.host = 'localhost'
        self.database = database
        self.port = port
        self.user = user
        self.password = password

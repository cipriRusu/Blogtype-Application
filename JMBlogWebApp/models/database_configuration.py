class DatabaseConfiguration:
    def __init__(self, host, database, port, user, password):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password

    def get_dictionary(self, exclude=None):
        if exclude is not None:
            self.__dict__.pop(exclude, None)
            return self.__dict__
        return self.__dict__

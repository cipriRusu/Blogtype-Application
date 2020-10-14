import psycopg2

class DbSetup():
    def __init__(self, connection_params):
        self._connection = psycopg2.connect(**connection_params)
        self._connection.autocommit = True
        self._cursor = self._connection.cursor()

    def execute_query(self, query, args=None):
        if args is None:
            self._cursor.execute(query)
        else:
            self._cursor.execute(query, args)
        return self._cursor

    def close_connection(self):
        self._cursor.close()
        self._connection.commit()
        self._connection.close()

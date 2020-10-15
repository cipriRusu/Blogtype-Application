import psycopg2
import setup.postgres_scripts as scripts

class DbSetup():
    def __init__(self, connection_params):
        self._params = connection_params
        self._connection = self._create_connection()
        self._cursor = self._connection.cursor()

    def execute_query(self, query, args=None):
        if args is None:
            self._cursor.execute(query)
        else:
            self._cursor.execute(query, args)
        return self._cursor

    def _create_connection(self):
        temp_connection = psycopg2.connect(
            host=self._params['host'],
            user=self._params['user'],
            password=self._params['password'])

        temp_connection.autocommit = True

        temp_cursor = temp_connection.cursor()

        temp_cursor.execute(scripts.LIST_DATABASES_SCRIPT)

        contained = temp_cursor.fetchall()

        databases = [x[0] for x in contained]

        #check if database exists on server
        if self._params.get('database') not in databases:
            temp_cursor.execute(scripts.CREATE_DATABASE_SCRIPT % self._params['database'])

            temp_cursor.close()
            temp_connection.commit()
            temp_connection.close()

            temp_connection = psycopg2.connect(
                host=self._params['host'],
                user=self._params['user'],
                database=self._params['database'],
                password=self._params['password'])

            temp_cursor = temp_connection.cursor()
            temp_cursor.execute(scripts.CREATE_TABLE_SCRIPT)

            temp_cursor.close()
            temp_connection.commit()
            temp_connection.close()

        #check if posts table exists in existing database
        temp_connection = psycopg2.connect(
            host=self._params['host'],
            user=self._params['user'],
            database=self._params['database'],
            password=self._params['password'])

        temp_cursor = temp_connection.cursor()

        temp_cursor.execute(scripts.SEARCH_TABLE_SCRIPT % ("'posts'",))

        if not temp_cursor.fetchone()[0]:
            temp_cursor.execute(scripts.CREATE_TABLE_SCRIPT)
            temp_cursor.close()
            temp_connection.commit()
            temp_connection.close()


        return psycopg2.connect(
            host=self._params['host'],
            user=self._params['user'],
            database=self._params['database'],
            password=self._params['password'])

    def close_connection(self):
        self._cursor.close()
        self._connection.commit()
        self._connection.close()

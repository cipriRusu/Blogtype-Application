import psycopg2

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

        temp_cursor.execute('SELECT datname from pg_database')

        contained = temp_cursor.fetchall()

        databases = [x[0] for x in contained]

        if self._params.get('database') not in databases:
            temp_cursor.execute("CREATE DATABASE %s;" % self._params['database'])

            temp_cursor.close()
            temp_connection.commit()
            temp_connection.close()

            temp_connection = psycopg2.connect(
                host=self._params['host'],
                user=self._params['user'],
                database=self._params['database'],
                password=self._params['password'])

            temp_cursor = temp_connection.cursor()
            temp_cursor.execute("CREATE TABLE POSTS(posts_id uuid,\
            creation_date timestamp,\
            edit_date timestamp,\
            author varchar,\
            title varchar,\
            post_content varchar);")

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

from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository
from setup.db_connection_setup import DBConnectionSetup

class PostsDBRepository(PostsRepository):
    def __init__(self):
        pass

    def add_post(self, item):
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('setup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute("INSERT INTO POSTS \
        (post_id, datetime, author, title, content_field) \
        VALUES(%s, %s, %s, %s, %s)",(
            str(item.post_id),
            item.datetime,
            item.author,
            item.title,
            item.content))

        conn.close_connection(current_connection, current_cursor)

    def get_all(self):
        all_elements = []
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('setup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute('SELECT * FROM POSTS;')

        for item in current_cursor.fetchall():
            element = BlogPost(*item)
            all_elements.append(element)

        conn.close_connection(current_connection, current_cursor)

        return all_elements


    def get_by_id(self, index):
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('setup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute("SELECT * FROM POSTS WHERE post_id=%s;", (str(index),))
        current_element = current_cursor.fetchone()
        conn.close_connection(current_connection, current_cursor)

        return BlogPost(*current_element)

    def remove(self, index):
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('setup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute("DELETE FROM POSTS WHERE post_id=%s;", (str(index),))
        conn.close_connection(current_connection, current_cursor)

from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository
from dbSetup.db_connection_setup import DBConnectionSetup

class PostsDBRepository(PostsRepository):
    def __init__(self):
        pass

    def add_post(self, item):
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('dbSetup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute("INSERT INTO POSTS(post_id, datetime, author, title, content_field) VALUES(%s, %s, %s, %s, %s)", 
                               (str(item.post_id), item.datetime, item.author, item.title, item.content))
        current_connection.commit()

    def get_all(self):
        db = []
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('dbSetup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute('SELECT * FROM POSTS;')

        for item in current_cursor.fetchall():
            element = BlogPost(*item)
            db.append(element)

        conn.close_connection(current_connection, current_cursor)
        return db


    def get_by_id(self, index):
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('dbSetup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute("SELECT * FROM POSTS WHERE post_id=%s;", (str(index),))
        current_element = current_cursor.fetchone()
        conn.close_connection(current_connection, current_cursor)
        return BlogPost(*current_element)

    def remove(self, index):
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('dbSetup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute("DELETE FROM POSTS WHERE post_id=%s;", (str(index),))
        current_connection.commit()

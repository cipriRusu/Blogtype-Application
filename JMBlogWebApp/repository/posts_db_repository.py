from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository
from dbSetup.db_connection_setup import DBConnectionSetup

class PostsDBRepository(PostsRepository):
    def __init__(self):
        pass

    def add_post(self, item):
        pass

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
        pass

    def remove(self, index):
        pass
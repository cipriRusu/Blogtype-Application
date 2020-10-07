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
        (posts_id,\
        creation_date,\
        edit_date,\
        author,\
        title,\
        post_content)\
        VALUES(%s, %s, %s, %s, %s, %s)", (
            str(item.post_id),
            item.stamp.creation_time,
            item.stamp.edit_time,
            item.author,
            item.title,
            item.content))

        conn.close_connection(current_connection, current_cursor)

    def update_post(self, item):
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('setup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute("UPDATE POSTS SET\
                                creation_date = %s,\
                                edit_date = %s,\
                                author = %s,\
                                title = %s,\
                                post_content = %s \
                                WHERE posts_id =%s;",
                               (item.stamp.creation_time,
                                item.stamp.edit_time,
                                item.author,
                                item.title,
                                item.content,
                                item.post_id))

        conn.close_connection(current_connection, current_cursor)

    def get_all(self):
        all_elements = []
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('setup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute('SELECT * FROM POSTS;')

        for item in current_cursor.fetchall():
            element = BlogPost(item[3], item[4], item[5])
            element.post_id = item[0]
            element.stamp.creation_time = item[1]
            element.stamp.edit_time = item[2]

            all_elements.append(element)

        conn.close_connection(current_connection, current_cursor)

        return all_elements

    def get_by_id(self, index):
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('setup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute("SELECT * FROM POSTS WHERE posts_id=%s;", (str(index),))
        item = current_cursor.fetchone()
        conn.close_connection(current_connection, current_cursor)

        element = BlogPost(
            item[3],
            item[4],
            item[5])

        element.post_id = item[0]
        element.stamp.creation_time = item[1]
        element.stamp.edit_time = item[2]

        return element

    def remove(self, index):
        conn = DBConnectionSetup()
        current_connection = conn.get_connection('setup/database.ini', 'postgresql_conn_data')
        current_cursor = current_connection.cursor()
        current_cursor.execute("DELETE FROM POSTS WHERE posts_id=%s;", (str(index),))
        conn.close_connection(current_connection, current_cursor)

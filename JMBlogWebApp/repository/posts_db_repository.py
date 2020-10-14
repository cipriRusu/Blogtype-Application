from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository
from setup.db_setup import DbSetup 
from setup.config import Config

class PostsDBRepository(PostsRepository):
    def __init__(self):
        self._params = Config().from_file('db_connection')
        self._conn = DbSetup(self._params)

    def add_post(self, item):
        self._conn.execute_query("INSERT INTO POSTS \
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

        self._conn.close_connection()

    def update_post(self, item):
        self._conn.execute_query("UPDATE POSTS SET\
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

        self._conn.close_connection()

    def get_all(self):
        all_elements = []
        query_result = self._conn.execute_query('SELECT * FROM POSTS;')

        for item in query_result.fetchall():
            element = BlogPost(
                item[3],
                item[4],
                item[5])

            element.post_id = item[0]
            element.stamp.creation_time = item[1]
            element.stamp.edit_time = item[2]

            all_elements.append(element)

        self._conn.close_connection()

        return all_elements

    def get_by_id(self, index):
        query_result = self._conn.execute_query('SELECT * FROM\
        POSTS WHERE posts_id=%s;', (str(index),))

        item = query_result.fetchone()
        self._conn.close_connection()

        element = BlogPost(
            item[3],
            item[4],
            item[5])

        element.post_id = item[0]
        element.stamp.creation_time = item[1]
        element.stamp.edit_time = item[2]

        return element

    def remove(self, index):
        self._conn.execute_query("DELETE FROM POSTS WHERE posts_id=%s;", (str(index),))
        self._conn.close_connection()

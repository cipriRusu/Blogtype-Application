from models.sqa_models.sqa_posts import Posts
from models.sqa_models.sqa_users import Users
from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository

class PostsDBRepository(PostsRepository):
    def __init__(self, db_connection):
        self._conn = db_connection

    def add_post(self, item):
        self._conn.start_session()

        session = self._conn.get_session()

        post_to_add = Posts()

        post_to_add.posts_id = str(item.post_id)
        post_to_add.creation_date = item.stamp.creation_time
        post_to_add.edit_date = item.stamp.edit_time
        post_to_add.author = item.author
        post_to_add.title = item.title
        post_to_add.post_content = item.content
        post_to_add.image_path = item.img_path

        session.add(post_to_add)

        self._conn.close_session()

    def update_post(self, item):
        self._conn.start_session()

        session = self._conn.get_session()

        (session.query(Posts)
         .filter(Posts.posts_id == item.post_id)
         .update({Posts.title: item.title,
                  Posts.post_content: item.content,
                  Posts.creation_date: item.stamp.creation_time,
                  Posts.edit_date: item.stamp.edit_time,
                  Posts.image_path: item.img_path}))

        self._conn.close_session()

    def get_all(self, filter_by=None):
        all_elements = []
        self._conn.start_session()

        session = self._conn.get_session()

        join_result = (session.query(Posts)
                       .join(Users, Posts.author == Users.user_id)
                       .values(Posts.posts_id,
                               Posts.title,
                               Users.user_name,
                               Posts.post_content,
                               Posts.creation_date,
                               Posts.edit_date,
                               Posts.image_path))

        for item in join_result:
            if (filter_by is None) or (filter_by == item.user_name):
                element = BlogPost(item.title,
                                   item.user_name,
                                   item.post_content,
                                   item.image_path)

                element.post_id = item.posts_id
                element.stamp.creation_time = item.creation_date
                element.stamp.edit_time = item.edit_date

                all_elements.append(element)

        self._conn.close_session()

        return all_elements

    def get_by_id(self, index):
        self._conn.start_session()

        session = self._conn.get_session()

        join_result = (session.query(Posts)
                       .join(Users, Posts.author == Users.user_id)
                       .filter(Posts.posts_id == index.hex)
                       .values(Posts.posts_id,
                               Posts.title,
                               Users.user_name,
                               Posts.post_content,
                               Posts.creation_date,
                               Posts.edit_date,
                               Posts.image_path))

        item = next(join_result)

        blog_post = BlogPost(item.title,
                             item.user_name,
                             item.post_content,
                             item.image_path)

        blog_post.post_id = item.posts_id
        blog_post.stamp.creation_time = item.creation_date
        blog_post.stamp.edit_time = item.edit_date

        self._conn.close_session()

        return blog_post

    def remove(self, index):
        self._conn.start_session()

        session = self._conn.get_session()

        (session.query(Posts)
         .filter(Posts.posts_id == index.hex)
         .delete(synchronize_session=False))

        self._conn.close_session()

from exceptions.post_not_found_exception import PostNotFoundException
from models.sqa_models.sqa_posts import Posts
from models.sqa_models.sqa_users import Users
from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository

class PostsDBRepository(PostsRepository):
    def __init__(self, db_connection, image_db):
        self._conn = db_connection
        self._image_db = image_db

    def add_post(self, item):
        self._conn.start_session()

        session = self._conn.get_session()

        post_to_add = Posts()

        post_to_add.posts_id = str(item.post_id)
        post_to_add.creation_date = item.stamp.creation_time
        post_to_add.edit_date = item.stamp.creation_time
        post_to_add.author = item.author
        post_to_add.title = item.title
        post_to_add.post_content = item.content
        post_to_add.image_path = self._image_db.add_image(item)

        session.add(post_to_add)

        self._conn.close_session()

    def update_post(self, blog_post, remove_image=False, update_image=False):
        self._conn.start_session()

        session = self._conn.get_session()

        (session.query(Posts)
         .filter(Posts.posts_id == blog_post.post_id)
         .update({Posts.title: blog_post.title,
                  Posts.post_content: blog_post.content,
                  Posts.creation_date: blog_post.stamp.creation_time,
                  Posts.edit_date: blog_post.stamp.edit_time,
                  Posts.image_path: self._image_db.update_image(blog_post,
                                                                remove_image,
                                                                update_image)}))

        self._conn.close_session()

    def get_all(self, filter_by=None):
        all_elements = []
        self._conn.start_session()

        session = self._conn.get_session()

        join_result = (session.query(Posts)
                       .join(Users, Posts.author == Users.user_id)
                       .order_by(Posts.edit_date)
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
                element.img_path = self._image_db.get_image(element)

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

        try:
            item = next(join_result)
        except Exception:
            raise PostNotFoundException

        blog_post = BlogPost(item.title,
                             item.user_name,
                             item.post_content,
                             item.image_path)

        blog_post.post_id = item.posts_id
        blog_post.stamp.creation_time = item.creation_date
        blog_post.stamp.edit_time = item.edit_date
        blog_post.img_path = self._image_db.get_image(blog_post)

        self._conn.close_session()

        return blog_post

    def remove(self, index):
        post_to_remove = self.get_by_id(index)
        self._image_db.remove_image(post_to_remove)

        self._conn.start_session()
        session = self._conn.get_session()

        (session.query(Posts)
         .filter(Posts.posts_id == index.hex)
         .delete(synchronize_session=False))

        self._conn.close_session()

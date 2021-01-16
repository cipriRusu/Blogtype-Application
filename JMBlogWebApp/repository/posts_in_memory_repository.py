from exceptions.postnotfound_exception import PostNotFoundException
from exceptions.user_exception  import UserException
from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository

class PostsInMemoryRepository(PostsRepository):
    def __init__(self, db, users_db, images_db):
        self._db = db
        self._users_db = users_db
        self._images_db = images_db

    def __iter__(self):
        for post in self._db:
            yield post

    def add_post(self, item):
        for user in self._users_db:
            if user.user_id == item.author:
                item.img_path = self._images_db.add_image(item)
                item.stamp.edit_time = item.stamp.creation_time
                self._db.append(item)

    def update_post(self, blog_post, remove_image=False):
        for post in self._db:
            if post.post_id == blog_post.post_id:
                blog_post.author = post.author
                blog_post.img_path = self._images_db.update_image(blog_post, remove_image)
                self._db.remove(post)
        self._db.append(blog_post)

    def get_by_id(self, index):
        for element in self._db:
            if element.post_id == index:
                found_post = BlogPost(
                    element.title,
                    self._users_db.get_user_by_id(element.author).user_name,
                    element.content,
                    element.img_path)

                found_post.stamp.creation_time = element.stamp.creation_time
                found_post.stamp.edit_time = element.stamp.edit_time
                found_post.post_id = element.post_id
                found_post.img_path = self._images_db.get_image(found_post)
                return found_post
        raise PostNotFoundException()

    def get_all(self, filter_by=None):
        all_posts = []

        for post in self._db:
            try:
                str_author_name = self._users_db.get_user_by_id(post.author).user_name
            except UserException:
                continue

            if filter_by in (None, str_author_name):
                found_post = BlogPost(
                    post.title,
                    str_author_name,
                    post.content,
                    post.img_path)

                found_post.img_path = self._images_db.get_image(found_post)
                found_post.stamp.creation_time = post.stamp.creation_time
                found_post.stamp.edit_time = post.stamp.edit_time
                found_post.post_id = post.post_id
                all_posts.append(found_post)

        return all_posts

    def remove(self, index):
        for found_post in self._db:
            if found_post.post_id == index:
                self._images_db.remove_image(found_post)
                self._db.remove(found_post)

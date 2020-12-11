from exceptions.user_exception  import UserException
from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository

class PostsInMemoryRepository(PostsRepository):
    def __init__(self, db, users_db):
        self._db = db
        self._users_db = users_db

    def __iter__(self):
        for post in self._db:
            yield post

    def add_post(self, item):
        for user in self._users_db:
            if user.user_id == item.author:
                self._db.append(item)

    def update_post(self, item):
        for found_post in self._db:
            if found_post.post_id == item.post_id:
                updated_post = found_post
                self._db.remove(found_post)
                updated_post.update(item.title, item.content)
                self._db.append(updated_post)

    def get_by_id(self, index):
        for element in self._db:
            if element.post_id == index:
                found_post = BlogPost(
                    element.title,
                    self._users_db.get_user_by_id(element.author).user_name,
                    element.content)

                found_post.stamp.creation_time = element.stamp.creation_time
                found_post.stamp.edit_time = element.stamp.edit_time
                found_post.post_id = element.post_id
                return found_post
        raise Exception("no element found!")

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
                    post.content)

                found_post.stamp.creation_time = post.stamp.creation_time
                found_post.stamp.edit_time = post.stamp.edit_time
                found_post.post_id = post.post_id
                all_posts.append(found_post)

        return all_posts

    def remove(self, index):
        for found_post in self._db:
            if found_post.post_id == index:
                self._db.remove(found_post)

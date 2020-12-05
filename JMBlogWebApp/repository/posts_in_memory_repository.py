from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository

class PostsInMemoryRepository(PostsRepository):
    def __init__(self, db, users_db):
        self._db = db
        self._users_db = users_db

    def __iter__(self):
        for element in self._db:
            yield element

    def add_post(self, item):
        for user in self._users_db:
            if user.user_id == item.author:
                self._db.append(item)

    def update_post(self, item):
        for initial_post in self._db:
            if initial_post.post_id == item.post_id:
                updated_post = BlogPost(
                    item.title,
                    self._users_db.get_by_name(item.author).user_id,
                    item.content)

                updated_post.post_id = item.post_id

                self._db.remove(initial_post)
                self._db.append(updated_post)

    def get_by_id(self, index):
        for element in self._db:
            if element.post_id == index:
                found_post = BlogPost(
                    element.title,
                    self._users_db.get_user_by_id(element.author).user_name,
                    element.content)

                found_post.post_id = element.post_id
                return found_post

        raise Exception("no element found!")

    def get_all(self):
        all_posts = []

        for post in self._db:
            element = BlogPost(
                post.title,
                self._users_db.get_user_by_id(post.author).user_name,
                post.content)

            element.post_id = post.post_id
            all_posts.append(element)

        return all_posts

    def remove(self, index):
        for element in self._db:
            if element.post_id == index:
                self._db.remove(element)

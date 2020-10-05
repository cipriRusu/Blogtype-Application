import uuid
import datetime
from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository

class PostsInMemoryRepository(PostsRepository):
    def __init__(self):
        self._db = [BlogPost(uuid.uuid4(), datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S")
                             , "FirstTitle", "FirstAuthor", "Lorem Ipsum is simply dummy , \
        'text of the printing and typesetting industry. Lorem Ipsum has been the industry's , \
        standard dummy text ever since the 1500s, when an unknown printer took a galley of , \
        type and scrambled it to make a type specimen book. It has survived not only five centuries, , \
        but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised, in the, \
        1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop , \
        publishing software like Aldus PageMaker including versions of Lorem Ipsum."),

        BlogPost(uuid.uuid4(), datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S"),
                 "SecondTitle", "SecondAuthor", "Lorem Ipsum is simply dummy text of the, \
        printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since, \
        the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen , \
        book. It has survived not only five centuries, but also the leap into electronic typesetting, , \
        remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets , \
        containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker , ~\
        including versions of Lorem Ipsum."),

        BlogPost(uuid.uuid4(), datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S"),
                 "ThirdTitle", "ThirdAuthor", "Lorem Ipsum is simply dummy text of the printing ,\
        and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, , \
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived , \
        not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was, \
        popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently , \
        with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")]

    def __iter__(self):
        for element in self._db:
            yield element

    def add_post(self, item):
        self._db.append(item)

    def get_by_id(self, index):
        for element in self._db:
            if element.post_id == index:
                return element
        raise Exception("no element found!")

    def get_all(self):
        return self._db

    def remove(self, index):
        for element in self._db:
            if element.post_id == index:
                self._db.remove(element)

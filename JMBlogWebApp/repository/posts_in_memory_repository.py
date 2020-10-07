import uuid
from models.blog_post import BlogPost
from repository.posts_repository import PostsRepository

class PostsInMemoryRepository(PostsRepository):
    def __init__(self):
        self._db = [BlogPost("FirstTitle", "FirstAuthor", "Lorem Ipsum is simply dummy ,\
                             'text of the printing and typesetting industry. Lorem Ipsum \
                             has been the industry's , standard dummy text ever since the \
                             1500s,when an unknown printer took a galley of , type and scrambled \
                             it to make a type specimen book. It has survived not only five \
                             centuries, but also the leap into electronic typesetting, \
                             remaining essentially unchanged. It was popularised, in the,\
                             1960s with the release of Letraset sheets containing Lorem Ipsum \
                             passages,and more recently with desktop , publishing software like \
                             Aldus PageMaker including versions of Lorem Ipsum."),

                    BlogPost("SecondTitle", "SecondAuthor", "Lorem Ipsum is simply \
                             dummy text of the, printing and typesetting industry. \
                             Lorem Ipsum has been the industry's standard dummy text \
                             ever since, the 1500s, when an unknown printer took a galley\
                             of type and scrambled it to make a type specimen book. \
                             It has survived not only five centuries, but also the leap\
                             into electronic typesetting, remaining essentially unchanged.\
                             It was popularised in the 1960s with the release of Letraset sheets , \
                             containing Lorem Ipsum passages, and more recently with desktop \
                             publishing software like Aldus PageMaker , including versions \
                             of Lorem Ipsum."),

                    BlogPost("ThirdTitle", "ThirdAuthor", "Lorem Ipsum is simply \
                             dummy text of the printing ,and typesetting industry.\
                             Lorem Ipsum has been the industry's standard dummy text\
                             ever since the 1500s,when an unknown printer took a galley\
                             of type and scrambled it to make a type specimen book. It has \
                             survived ,not only five centuries, but also the leap into \
                             electronic typesetting, remaining essentially unchanged. It was \
                             popularised in the 1960s with the release of Letraset sheets \
                             containing Lorem Ipsum passages, and more recently , with desktop \
                             publishing software like Aldus PageMaker including \
                             versions of Lorem Ipsum.")]

        self._db[0].post_id = uuid.UUID('f9c3a576-28bc-4b63-931d-04d6488d2f0d')
        self._db[0].stamp.creation_time = '2019-09-03 19:40:33'

        self._db[1].post_id = uuid.UUID('daca57d1-c180-4e0a-8394-f5c95a5d5f23')
        self._db[1].stamp.creation_time = '1991-03-02 12:30:44'

        self._db[2].post_id = uuid.UUID('a656f973-5b82-462d-aff7-8d2c6c3e4fa2')
        self._db[2].stamp.creation_time = '2017-04-05 21:40:32'

    def __iter__(self):
        for element in self._db:
            yield element

    def add_post(self, item):
        self._db.append(item)

    def update_post(self, item):
        self._db.remove(item)
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
            if element.stamp.post_id == index:
                self._db.remove(element)

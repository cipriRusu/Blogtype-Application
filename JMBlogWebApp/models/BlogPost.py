# pylint: disable=locally-disabled, multiple-statements, missing-module-docstring, missing-class-docstring
import uuid

class BlogPost:
    def __init__(self, author, title, content):
        self.id = uuid.uuid4()
        self.author = author
        self.title = title
        self.content = content

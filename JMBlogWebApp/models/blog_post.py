import uuid
from models.timestamp import TimeStamp

class BlogPost:
    def __init__(self, title, author, content):
        self.post_id = uuid.uuid4()
        self.stamp = TimeStamp()
        self.author = author
        self.title = title
        self.content = content
        self.preview = content[0:30]

    def __eq__(self, other):
        return self.post_id == other.post_id

    def update(self, title, content):
        self.title = title
        self.content = content
        self.preview = content[0:30]
        self.stamp.on_edit()

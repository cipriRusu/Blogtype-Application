import uuid
from models.timestamp import TimeStamp

class BlogPost:
    def __init__(self, title, author, content, img_path):
        self.post_id = uuid.uuid4()
        self.stamp = TimeStamp()
        self.author = author
        self.title = title
        self.content = content
        self.preview = content[0:30]
        self.img_path = img_path

    def __eq__(self, other):
        return self.post_id == other.post_id

    def update(self, title=None, content=None, img_path=None):
        self.title = title if title is not None else self.title
        self.content = content if content is not None else self.title
        self.img_path = img_path
        self.preview = self.content[0:30]
        self.stamp.on_edit()

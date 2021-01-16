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
        self.uploaded_file = None

    def __eq__(self, other):
        return self.post_id == other.post_id

    def update(self, title=None, content=None):
        self.title = title if title is not None else self.title
        self.content = content if content is not None else self.content
        self.preview = self.content[0:30]
        self.stamp.on_edit()

    def upload(self, uploaded_file):
        self.uploaded_file = uploaded_file

    def to_dict(self):
        return {'post_id': self.post_id,
                'timestamp': {'creation_time': self.stamp.creation_time,
                              'edit_time': self.stamp.edit_time},
                'author': self.author,
                'title': self.title,
                'content': self.content,
                'preview': self.preview,
                'image_path': self.img_path}

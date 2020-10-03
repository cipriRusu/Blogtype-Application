import uuid
import datetime
from itertools import islice

class BlogPost:
    def __init__(self, title, author, content):
        self.post_id = uuid.uuid4()
        self.datetime = datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S")
        self.author = author
        self.title = title
        self.content = content
        self.preview = ' '.join(list(islice(content.split(), 0, 10)))

    def __init__(self, post_id, datetime, author, title, content):
        self.post_id = post_id
        self.datetime = datetime
        self.author = author
        self.title = title
        self.content = content
        self.preview = ' '.join(list(islice(content.split(), 0, 10)))


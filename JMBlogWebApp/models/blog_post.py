from itertools import islice

class BlogPost:
    def __init__(self, post_id, datetime, title, author, content):
        self.post_id = post_id
        self.datetime = datetime
        self.author = author
        self.title = title
        self.content = content
        self.preview = ' '.join(list(islice(content.split(), 0, 10)))


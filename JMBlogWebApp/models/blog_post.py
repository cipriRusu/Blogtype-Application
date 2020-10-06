from models.post_id_and_timestamps import PostIdAndTimestamps

class BlogPost:
    def __init__(self, title, author, content):
        self.stamp = PostIdAndTimestamps()
        self.author = author
        self.title = title
        self.content = content
        self.preview = content[0:30]

    def __eq__(self, other):
        return self.stamp.post_id == other.stamp.post_id

    def update(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.stamp.on_edit()

class BlogPost:
    def __init__(self, post_id, datetime, title, author, content):
        self.post_id = post_id
        self.datetime = datetime
        self.author = author
        self.title = title
        self.content = content
        self.preview = content[0:30]
   
    def __eq__(self, other):
        return self.post_id == other.post_id

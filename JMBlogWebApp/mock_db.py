from models.blog_post import BlogPost

class MockDatabase:
    def __init__(self):
        self.db = [BlogPost("FirstTitle", "FirstAuthor", "Lorem Ipsum is simply dummy , \
        'text of the printing and typesetting industry. Lorem Ipsum has been the industry's , \
        standard dummy text ever since the 1500s, when an unknown printer took a galley of , \
        type and scrambled it to make a type specimen book. It has survived not only five centuries, , \
        but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised, in the, \
        1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop , \
        publishing software like Aldus PageMaker including versions of Lorem Ipsum."),

        BlogPost("SecondTitle", "SecondAuthor", "Lorem Ipsum is simply dummy text of the, \
        printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since, \
        the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen , \
        book. It has survived not only five centuries, but also the leap into electronic typesetting, , \
        remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets , \
        containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker , ~\
        including versions of Lorem Ipsum."),

        BlogPost("ThirdTitle", "ThirdAuthor", "Lorem Ipsum is simply dummy text of the printing , \
        and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, , \
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived , \
        not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was, \
        popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently , \
        with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")]

    def __iter__(self):
        for element in self.db:
            yield element

    def AddPost(self, blog_post):
        self.db.append(blog_post)
    
    def GetByIndex(self, post_id):
        for element in self.db:
            if element.post_id == post_id:
                return element

    def GetAll(self):
        return self.db

    def Remove(self, current_index):
        for element in self.db:
            if element.post_id == current_index:
                self.db.remove(element)
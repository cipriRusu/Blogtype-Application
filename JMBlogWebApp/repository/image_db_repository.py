import os
from flask import url_for
from repository.image_repository import ImageRepository

LEGAL_EXTENSIONS = ['.jpg', '.jpeg', '.png']

class ImageDbRepository(ImageRepository):
    def __init__(self):
        pass

    def add_image(self, blog_post):
        pass

    def update_image(self, old_blogpost, blog_post, remove_image=False):
        pass

    def remove_image(self, blog_post):

        os.remove(os.path.join('static', blog_post.img_path))

        blog_post.update(img_path=None)

    def get_image(self, blog_post):
        if (blog_post.img_path is None or not
                os.path.exists(os.path.join('static/images/' + blog_post.img_path))):
            return url_for('static', filename='images/default.png')
        return url_for('static', filename='images/' + blog_post.img_path)

import os
from flask import url_for
from repository.image_repository import ImageRepository

class ImageDbRepository(ImageRepository):
    def __init__(self):
        pass

    def add_image(self, blog_post, added_image):
        if added_image.filename != '':
            added_image.save(os.path.join('static/images', added_image.filename))
            blog_post.img_path = 'images/{}'.format(added_image.filename)

    def remove_image(self, blog_post):
        if (blog_post.img_path is not None and
            os.path.exists(os.path.join('static', blog_post.img_path))):
            os.remove(os.path.join('static', blog_post.img_path))
        blog_post.img_path = None

    def get_image(self, blog_post):
        if (blog_post.img_path is None or not
                os.path.exists(os.path.join('static', blog_post.img_path))):
            return url_for('static', filename='images/default.png')
        return url_for('static', filename=blog_post.img_path)

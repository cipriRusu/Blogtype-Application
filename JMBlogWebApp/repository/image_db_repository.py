import os
import uuid
from flask import url_for, flash
from repository.image_repository import ImageRepository

LEGAL_EXTENSIONS = ['.jpg', '.jpeg', '.png']

class ImageDbRepository(ImageRepository):
    def __init__(self):
        pass

    def add_image(self, blog_post):
        if blog_post.uploaded_file.filename == '':
            return None

        current_file = str(uuid.uuid4())[:4] + '_' + blog_post.uploaded_file.filename
        source_path = os.path.join('static/images/', current_file)
        blog_post.uploaded_file.save(source_path)

        if blog_post.img_path != None and blog_post.img_path != '/images/default.png':
            if os.path.exists(os.path.join('static' + blog_post.img_path)):
                os.remove(os.path.join('static' + blog_post.img_path))
        return current_file

    def update_image(self, blog_post, remove_image=False):
        if remove_image:
            if blog_post.img_path != '/images/default.png':
                return self.remove_image(blog_post)
            flash('No photo found, nothing to remove')
            return None

        updated_image = self.add_image(blog_post)

        if updated_image is None:
            flash('No image uploaded')
            return blog_post.img_path[8:]
        return updated_image

    def remove_image(self, blog_post):
        os.remove(os.path.join('static' + blog_post.img_path))
        return None

    def get_image(self, blog_post):
        if (blog_post.img_path is None or not
                os.path.exists(os.path.join('static/images/' + blog_post.img_path))):
            return url_for('static', filename='images/default.png')
        return url_for('static', filename='images/' + blog_post.img_path)

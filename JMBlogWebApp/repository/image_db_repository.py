import os
import uuid
from exceptions.filepath_exception import FilePathException
from exceptions.fileformat_exception import FileFormatException
from flask import url_for
from repository.image_repository import ImageRepository

LEGAL_EXTENSIONS = ['.jpg', '.jpeg', '.png']

class ImageDbRepository(ImageRepository):
    def __init__(self):
        pass

    def add_image(self, blog_post, added_image):
        if added_image.filename == '':
            raise FilePathException()

        if added_image.filename[-4:].lower() not in LEGAL_EXTENSIONS:
            raise FileFormatException()

        source_path = os.path.join('static/images', added_image.filename)

        if os.path.exists(source_path):
            alternative_filename = str(uuid.uuid4())[:4] + '_' + added_image.filename
            source_path = os.path.join('static/images', alternative_filename)
            added_image.filename = alternative_filename
        added_image.save(source_path)
        blog_post.update(img_path='images/{}'.format(added_image.filename))

    def remove_image(self, blog_post):
        if blog_post.img_path is None:
            raise FilePathException()

        if not os.path.exists(os.path.join('static', blog_post.img_path)):
            raise FilePathException()

        os.remove(os.path.join('static', blog_post.img_path))
        blog_post.img_path = None

    def get_image(self, blog_post):
        if (blog_post.img_path is None or not
                os.path.exists(os.path.join('static', blog_post.img_path))):
            return url_for('static', filename='images/default.png')
        return url_for('static', filename=blog_post.img_path)

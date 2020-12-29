import base64
from exceptions.fileformat_exception import FileFormatException
from exceptions.filepath_exception import FilePathException
from flask import url_for
from repository.image_repository import ImageRepository
from repository.in_memory_data import in_memory_photos

LEGAL_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.img']

class ImageInMemoryRepository(ImageRepository):
    COUNTER = 0
    def __init__(self):
        pass

    def add_image(self, blog_post, added_image):
        if added_image.filename == '':
            raise FilePathException()

        if added_image.filename[-4:].lower() not in LEGAL_EXTENSIONS:
            raise FileFormatException()

        current_pic = base64.b64encode(added_image.read())

        if 'images/'+ added_image.filename in in_memory_photos:
            alternative_filename = str(ImageInMemoryRepository.COUNTER) + added_image.filename
            added_image.filename = alternative_filename
            ImageInMemoryRepository.COUNTER = ImageInMemoryRepository.COUNTER + 1

        in_memory_photos['images/'+ added_image.filename] = current_pic.decode("utf-8")
        blog_post.img_path = 'images/{}'.format(added_image.filename)

    def remove_image(self, blog_post):
        if blog_post.img_path == '':
            raise FilePathException()

        if blog_post.img_path is None:
            raise FilePathException()

        del in_memory_photos[blog_post.img_path]
        blog_post.img_path = None

    def get_image(self, blog_post):
        if blog_post.img_path is None or blog_post.img_path not in in_memory_photos:
            return url_for('static', filename='images/default.png')
        return "data:image/jpeg;charset=utf-8;base64, "+ in_memory_photos[blog_post.img_path]

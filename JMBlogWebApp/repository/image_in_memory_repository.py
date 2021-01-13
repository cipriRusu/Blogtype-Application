import base64
import uuid
from repository.image_repository import ImageRepository
from repository.in_memory_data import in_memory_photos

LEGAL_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.img']

class ImageInMemoryRepository(ImageRepository):
    COUNTER = 0
    def __init__(self):
        pass

    def add_image(self, blog_post):
        pass

    def update_image(self, blog_post, remove_image=False):
        pass

    def remove_image(self, blog_post):
        pass

    def get_image(self, blog_post):
        if blog_post.img_path is None or blog_post.img_path not in in_memory_photos:
            return "data:image/jpeg;charset=utf-8;base64, "+ in_memory_photos['default']
        return "data:image/jpeg;charset=utf-8;base64, "+ in_memory_photos[blog_post.img_path]

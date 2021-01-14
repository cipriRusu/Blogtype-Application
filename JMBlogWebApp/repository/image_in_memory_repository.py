import base64
import uuid
from flask import flash
from repository.image_repository import ImageRepository
from repository.in_memory_data import in_memory_photos

LEGAL_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.img']

class ImageInMemoryRepository(ImageRepository):
    def __init__(self):
        #TODO:Refactor repeating code blocks
        pass

    def add_image(self, blog_post):
        uploaded = blog_post.img_path.read()

        if uploaded == b'':
            return None
        current_pic = base64.b64encode(uploaded)
        filename = str(uuid.uuid4())[:4] + '_' + blog_post.img_path.filename
        in_memory_photos[filename] = current_pic.decode('utf-8')
        return filename

    def update_image(self, old_blogpost, blog_post, remove_image=False):
        uploaded = blog_post.img_path.read()

        if remove_image is True:
            if old_blogpost.img_path is not None:
                del in_memory_photos[old_blogpost.img_path]
                return None

        if uploaded == b'':
            flash("No image found!")
        current_pic = base64.b64encode(uploaded)
        filename = str(uuid.uuid4())[:4] + '_' + blog_post.img_path.filename
        in_memory_photos[filename] = current_pic.decode('utf-8')
        return filename

    def remove_image(self, blog_post):
        if blog_post.img_path is not None:
            del in_memory_photos[blog_post.img_path]
            return None
        return None

    def get_image(self, blog_post):
        if blog_post.img_path is None or blog_post.img_path not in in_memory_photos:
            return "data:image/jpeg;charset=utf-8;base64, "+ in_memory_photos['default']
        return "data:image/jpeg;charset=utf-8;base64, "+ in_memory_photos[blog_post.img_path]

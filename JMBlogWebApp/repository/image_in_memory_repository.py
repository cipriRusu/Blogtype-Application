import base64
import uuid
import os
from flask import flash
from repository.image_repository import ImageRepository
from repository.in_memory_data import in_memory_photos

LEGAL_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.img']

class ImageInMemoryRepository(ImageRepository):
    def __init__(self):
        pass

    def add_image(self, blog_post):
        uploaded = blog_post.uploaded_file.read()

        if uploaded == b'':
            return None

        if (os.path.splitext(blog_post.uploaded_file.filename)[1].lower()
                not in LEGAL_EXTENSIONS):
            flash('Invalid file type! Make sure a valid file format is selected')
            return None

        current_pic = base64.b64encode(uploaded)
        filename = str(uuid.uuid4())[:4] + '_' + blog_post.uploaded_file.filename
        in_memory_photos[filename] = current_pic.decode('utf-8')
        return filename

    def update_image(self, blog_post, remove_image=False, update_image=False):
        if remove_image:
            if blog_post.img_path.split()[1] != in_memory_photos['default']:
                return self.remove_image(blog_post)
            flash('No photo found, nothing to remove')
            return None

        updated_image = self.add_image(blog_post)

        if updated_image is None:
            if update_image is True:
                flash('No image uploaded')
            return blog_post.img_path[8:]
        return updated_image

    def remove_image(self, blog_post):
        for image in in_memory_photos:
            if blog_post.img_path == image:
                del in_memory_photos[blog_post.img_path]
                return None
        return Exception()

    def get_image(self, blog_post):
        if blog_post.img_path is None or blog_post.img_path not in in_memory_photos:
            return "data:image/jpeg;charset=utf-8;base64, "+ in_memory_photos['default']
        return "data:image/jpeg;charset=utf-8;base64, "+ in_memory_photos[blog_post.img_path]

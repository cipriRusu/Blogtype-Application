import base64
import uuid
from exceptions.fileformat_exception import FileFormatException
from exceptions.filepath_exception import FilePathException
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

        filename = str(uuid.uuid4())[:4] + '_' + added_image.filename

        in_memory_photos['images/' + filename] = current_pic.decode("utf-8")

        blog_post.img_path = 'images/{}'.format(filename)

    def update_image(self, old_post, new_post):

        #TODO:update new post with old post data

        uploaded_image = base64.b64encode(new_post.img_path.read())

        new_post.author = old_post.author

        return new_post

    def remove_image(self, blog_post):
        if blog_post.img_path == '':
            raise FilePathException()

        if blog_post.img_path is None:
            raise FilePathException()

        del in_memory_photos[blog_post.img_path]
        blog_post.img_path = None

    def get_image(self, blog_post):
        if blog_post.img_path is None or blog_post.img_path not in in_memory_photos:
            return "data:image/jpeg;charset=utf-8;base64, "+ in_memory_photos['default']
        return "data:image/jpeg;charset=utf-8;base64, "+ in_memory_photos[blog_post.img_path]

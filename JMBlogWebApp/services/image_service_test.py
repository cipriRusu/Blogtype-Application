import base64
import os
import uuid
from repository.in_memory_data import in_memory_photos

class ImageServiceTest():
    def __init__(self):
        pass

    def upload_image(self, content):

        current_pic = base64.b64encode(content.read())

        filename = str(uuid.uuid4())[:4] + '_' + content.filename

        in_memory_photos[filename] = current_pic.decode('utf-8')
       
        return filename

    def remove_image(self, file_name):
        pass

import base64
import os
import uuid

class ImageServiceDb():
    def __init__(self):
        pass

    def upload_image(self, content):

        current_file = str(uuid.uuid4())[:4] + '_' + content.filename

        source_path = os.path.join('static/images/', current_file)

        content.save(source_path)

        return current_file

    def remove_image(self, file_name):
        
        os.remove('static' + file_name)

        return None


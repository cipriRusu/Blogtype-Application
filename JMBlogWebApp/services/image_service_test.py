import base64
import os
import uuid
from flask import flash
from repository.in_memory_data import in_memory_photos

class ImageServiceTest():
    def __init__(self):
        pass

    def upload_image(self, content):

        uploaded = content.read()

        if uploaded == b'':
            flash('No file uploaded.')
        else:
            current_pic = base64.b64encode(uploaded)

            filename = str(uuid.uuid4())[:4] + '_' + content.filename

            in_memory_photos[filename] = current_pic.decode('utf-8')
       
            return filename

    def remove_image(self, file_name):
        for key, value in in_memory_photos.items():
            if value == file_name.split(" ")[1]:
                if key != 'default':
                    del[value]
                else:
                    flash('No image found. Nothing to remove')

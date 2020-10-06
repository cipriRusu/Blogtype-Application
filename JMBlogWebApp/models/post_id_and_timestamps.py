import uuid
import datetime

class PostIdAndTimestamps:
    def __init__(self):
        self.post_id = uuid.uuid4()
        self.creation_time = datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S")
        self.edit_time = None

    def on_edit(self):
        self.edit_time = datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S")

import uuid
import datetime

class PostIdAndTimestamps:
    def __init__(self):
        _current_time = datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S")
        self.post_id = uuid.uuid4()
        self.creation_time = _current_time
        self.edit_time = datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S")

    def on_edit(self):
        self.edit_time = datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S")

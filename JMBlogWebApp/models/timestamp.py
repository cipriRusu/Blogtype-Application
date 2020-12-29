import datetime

class TimeStamp:
    def __init__(self):
        self.creation_time = datetime.datetime.now().replace(microsecond=0)
        self.edit_time = None

    def on_edit(self):
        self.edit_time = datetime.datetime.now().replace(microsecond=0)

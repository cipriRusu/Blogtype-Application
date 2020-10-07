import datetime

class TimeStamp:
    def __init__(self):
        self.creation_time = datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S")
        self.edit_time = None

    def on_edit(self):
        self.edit_time = datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S")

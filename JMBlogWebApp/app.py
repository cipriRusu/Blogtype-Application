from flask import Flask
from views.post_manager import post_manager

app = Flask(__name__, static_url_path="", static_folder="static")
app.register_blueprint(post_manager)

if __name__ == '__main__':
    app.run('localhost', 4449)

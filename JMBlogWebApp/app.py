from flask import Flask, redirect
from views import post_manager
from views import setup_manager
from setup.config import Config

app = Flask(__name__, static_url_path="", static_folder="static")
app.register_blueprint(post_manager.post_manager)
app.register_blueprint(setup_manager.setup_manager)

@app.route('/')
@app.route('/<path:path>')
def catch_all():
    if Config().is_configured():
        return redirect('/posts/', 302)
    return redirect('/dbsetup/', 302)

if __name__ == '__main__':
    app.run('localhost', 4449)

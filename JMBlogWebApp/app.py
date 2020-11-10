import os
from flask import Flask, redirect
from views import post_manager
from views import setup_manager
from views import user_manager

app = Flask(__name__, static_url_path="", static_folder="static")
app.secret_key = os.urandom(10)

with app.app_context():
    app.register_blueprint(post_manager.post_manager)
    app.register_blueprint(setup_manager.setup_manager)
    app.register_blueprint(user_manager.user_manager)

    @app.route('/')
    @app.route('/<path:path>')
    def catch_all():
        return redirect('/setup', 302)

if __name__ == '__main__':
    app.run('localhost', 4449)

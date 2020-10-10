from os import path
from flask import Flask, redirect
from views import post_manager
from views import connection_manager

app = Flask(__name__, static_url_path="", static_folder="static")
app.register_blueprint(post_manager.post_manager)
app.register_blueprint(connection_manager.connection_manager)

@app.route('/')
@app.route('/<path:path>')
def catch_all():
    if path.exists('./setup/database.ini'):
        return redirect('/posts/', 302)
    return redirect('/dbsetup/', 302)

if __name__ == '__main__':
    app.run('localhost', 4449)

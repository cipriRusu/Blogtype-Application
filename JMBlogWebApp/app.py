from flask import Flask, redirect
from views import post_manager

app = Flask(__name__, static_url_path="", static_folder="static")
app.register_blueprint(post_manager.post_manager)

@app.route('/')
@app.route('/<path:path>')
def catch_all():
    return redirect('/posts/', 302)

if __name__ == '__main__':
    app.run('localhost', 4449)

from flask import Flask, redirect
from views.post_manager import post_manager

app = Flask(__name__, static_url_path="", static_folder="static")
app.register_blueprint(post_manager)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect('/posts/allPosts', 302)

if __name__ == '__main__':
    app.run('localhost', 4449)

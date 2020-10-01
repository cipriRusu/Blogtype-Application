from flask import Blueprint, render_template, request, redirect, url_for
from models.blog_post import BlogPost
from repository.posts_in_memory_repository import PostsInMemoryRepository

repository = PostsInMemoryRepository()
post_manager = Blueprint('post_manager', __name__, template_folder='templates')

@post_manager.route('/', methods=["GET"])
def index():
    return render_template("index.html", database=repository.get_all())

@post_manager.route('/item/<uuid:current_index>')
def content(current_index):
    return render_template("Content.html", current=repository.get_by_id(current_index))

@post_manager.route('/addItem', methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        to_add = BlogPost(
            request.form['NameInput'],
            request.form['AuthorInput'],
            request.form['ContentInput'])
        repository.add_post(to_add)
        return redirect(url_for('.content', current_index=to_add.post_id))
    return render_template("AddItem.html")

@post_manager.route('/removeItem/<uuid:current_index>')
def remove_item(current_index):
    repository.remove(current_index)
    return redirect('/')

@post_manager.route('/updateItem/<uuid:current_index>', methods=["GET", "POST"])
def update_item(current_index):
    if request.method == "GET":
        return render_template("UpdateItem.html", current=repository.get_by_id(current_index))

    if request.method == "POST":
        repository.remove(current_index)
        edited = BlogPost(
            request.form['NameInput'],
            request.form['AuthorInput'],
            request.form['ContentInput'])
        repository.add_post(edited)
        return redirect(url_for('.content', current_index=edited.post_id))
    return Exception("Request type cannot be handled")

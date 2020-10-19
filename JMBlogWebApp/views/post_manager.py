from flask import Blueprint, render_template, request, redirect, url_for
from models.blog_post import BlogPost
from services.services import Services as src

post_manager = Blueprint('post_manager', __name__, url_prefix='/posts', template_folder='templates')

@post_manager.route('/', methods=["GET"])
def index():
    return render_template("list_posts.html", database=src().get_service('test').get_all())

@post_manager.route('/<uuid:current_index>')
def content(current_index):
    return render_template("view_post.html",
                           current=src().get_service('test').get_by_id(current_index))

@post_manager.route('/add', methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        to_add = BlogPost(
            request.form['NameInput'],
            request.form['AuthorInput'],
            request.form['ContentInput'])

        src().get_service('test').add_post(to_add)
        return redirect(url_for('.content', current_index=to_add.post_id))
    return render_template("add_post.html")

@post_manager.route('/remove/<uuid:current_index>')
def remove_item(current_index):
    src().get_service('test').remove(current_index)
    return redirect('/')

@post_manager.route('/update/<uuid:current_index>', methods=["GET", "POST"])
def update_item(current_index):
    if request.method == "GET":
        return render_template("update_post.html",
                               current=src().get_service('database').get_by_id(current_index))

    if request.method == "POST":
        current = src().get_service('database').get_by_id(current_index)
        current.update(
            request.form['NameInput'],
            request.form['AuthorInput'],
            request.form['ContentInput'])
        src().get_service('test').update_post(current)

        return redirect(url_for('.content', current_index=current.post_id))
    return Exception("Request type cannot be handled")

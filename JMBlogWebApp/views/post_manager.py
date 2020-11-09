from flask import Blueprint, render_template, request, redirect, url_for
from setup import services_listing as services
from models.blog_post import BlogPost
from decorators import decorators

post_manager = Blueprint('post_manager', __name__, url_prefix='/posts', template_folder='templates')

@post_manager.route('/', methods=["GET"])
@decorators.config_check
@decorators.inject
def index(current_database: services.DATA_SOURCE_POSTS):
    return render_template("list_posts.html", database=current_database.get_all())

@post_manager.route('/<uuid:current_index>')
@decorators.config_check
@decorators.inject
def content(current_index, current: services.DATA_SOURCE_POSTS):
    return render_template("view_post.html", current=current.get_by_id(current_index))

@post_manager.route('/add', methods=["GET", "POST"])
@decorators.config_check
@decorators.inject
def add_item(current_database: services.DATA_SOURCE_POSTS):
    if request.method == "POST":
        to_add = BlogPost(
            request.form['NameInput'],
            request.form['AuthorInput'],
            request.form['ContentInput'])
        current_database.add_post(to_add)
        return redirect(url_for('.content', current_index=to_add.post_id))
    return render_template("add_post.html")

@post_manager.route('/remove/<uuid:current_index>')
@decorators.config_check
@decorators.inject
def remove_item(current_index, current_database: services.DATA_SOURCE_POSTS):
    current_database.remove(current_index)
    return redirect('/posts')

@post_manager.route('/update/<uuid:current_index>', methods=["GET", "POST"])
@decorators.config_check
@decorators.inject
def update_item(current_index, current_database: services.DATA_SOURCE_POSTS):
    if request.method == "GET":
        return render_template("update_post.html",
                               current=current_database.get_by_id(current_index))

    if request.method == "POST":
        current = current_database.get_by_id(current_index)
        current.update(request.form['NameInput'],
                       request.form['AuthorInput'],
                       request.form['ContentInput'])
        current_database.update_post(current)
        return redirect(url_for('.content', current_index=current.post_id))
    return Exception("Request type cannot be handled")

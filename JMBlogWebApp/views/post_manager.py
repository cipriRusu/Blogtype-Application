from flask import Blueprint, render_template, request, redirect, url_for, session
from setup import services_listing as services
from models.blog_post import BlogPost
from views.decorators import setup_decorators
from views.decorators import inject_decorators
from views.decorators import authorization_decorators

post_manager = Blueprint('post_manager', __name__, url_prefix='/posts', template_folder='templates')

@post_manager.route('/', methods=["GET"])
@setup_decorators.config_check
@inject_decorators.inject
def index(current_database: services.DATA_SOURCE_POSTS,
          current_users: services.DATA_SOURCE_USERS):

    username_filter = None if "Users" not in request.args else request.args["Users"]

    return render_template("list_posts.html",
                           database=current_database.get_all(filter_by=username_filter),
                           users=current_users.get_users())

@post_manager.route('/<uuid:post_index>')
@setup_decorators.config_check
@inject_decorators.inject
def content(post_index, current: services.DATA_SOURCE_POSTS):
    return render_template("view_post.html", current=current.get_by_id(post_index))

@post_manager.route('/add', methods=["GET", "POST"])
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.requres_login
def add_item(current_database: services.DATA_SOURCE_POSTS):
    if request.method == "POST":
        to_add = BlogPost(
            request.form['NameInput'],
            session['logged_id'],
            request.form['ContentInput'])
        current_database.add_post(to_add)
        return redirect(url_for('.content', post_index=to_add.post_id))
    return render_template("add_post.html")

@post_manager.route('/remove/<uuid:post_index>')
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.requres_login
@authorization_decorators.admin_or_owner_required
def remove_item(post_index, current_database: services.DATA_SOURCE_POSTS):
    current_database.remove(post_index)
    return redirect('/posts')

@post_manager.route('/update/<uuid:post_index>', methods=["GET", "POST"])
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.requres_login
@authorization_decorators.admin_or_owner_required
def update_item(post_index, current_database: services.DATA_SOURCE_POSTS):
    if request.method == "GET":
        return render_template("update_post.html",
                               current=current_database.get_by_id(post_index))

    if request.method == "POST":
        current = current_database.get_by_id(post_index)

        current.update(request.form['NameInput'],
                       request.form['ContentInput'])

        current_database.update_post(current)
        return redirect(url_for('.content', post_index=current.post_id))
    return Exception("Request type cannot be handled")

from flask import Blueprint, render_template, request, redirect, url_for
from setup import services_listing as services
from models.blog_post import BlogPost
from services.services import Services
from decorators import decorators

post_manager = Blueprint('post_manager', __name__, url_prefix='/posts', template_folder='templates')

@post_manager.route('/', methods=["GET"])
@decorators.config_check
def index():
    return render_template("list_posts.html",
                           database=Services
                           .get_service(services.DATA_SOURCE)
                           .get_all())

@post_manager.route('/<uuid:current_index>')
@decorators.config_check
def content(current_index):
    return render_template("view_post.html",
                           current=Services
                           .get_service(services.DATA_SOURCE)
                           .get_by_id(current_index))

@post_manager.route('/add', methods=["GET", "POST"])
@decorators.config_check
def add_item():
    if request.method == "POST":
        to_add = BlogPost(
            request.form['NameInput'],
            request.form['AuthorInput'],
            request.form['ContentInput'])
        Services.get_service(services.DATA_SOURCE).add_post(to_add)
        return redirect(url_for('.content', current_index=to_add.post_id))
    return render_template("add_post.html")

@post_manager.route('/remove/<uuid:current_index>')
@decorators.config_check
def remove_item(current_index):
    Services.get_service(services.DATA_SOURCE).remove(current_index)
    return redirect('/posts')

@post_manager.route('/update/<uuid:current_index>', methods=["GET", "POST"])
@decorators.config_check
def update_item(current_index):
    if request.method == "GET":
        return render_template("update_post.html",
                               current=Services
                               .get_service(services.DATA_SOURCE)
                               .get_by_id(current_index))

    if request.method == "POST":
        current = Services.get_service(services.DATA_SOURCE).get_by_id(current_index)
        current.update(request.form['NameInput'],
                       request.form['AuthorInput'],
                       request.form['ContentInput'])
        Services.get_service(services.DATA_SOURCE).update_post(current)
        return redirect(url_for('.content', current_index=current.post_id))
    return Exception("Request type cannot be handled")

from exceptions.filepath_exception import FilePathException
from exceptions.fileformat_exception import FileFormatException
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from setup import services_listing as services
from models.blog_post import BlogPost
from views.decorators import setup_decorators
from views.decorators import inject_decorators
from views.decorators import authorization_decorators

post_manager = Blueprint('post_manager', __name__, url_prefix='/posts',
                         template_folder='templates',
                         static_folder='static')

@post_manager.route('/', methods=["GET"])
@setup_decorators.config_check
@inject_decorators.inject
def index(current_users: services.DATA_SOURCE_USERS,
          current_database: services.DATA_SOURCE_POSTS,
          pagination_factory: services.PAGINATION_FACTORY,
          image_source: services.DATA_SOURCE_IMAGES):

    pagination = pagination_factory.create_pagination(current_database,
                                                      request.args.get("Users"),
                                                      request.args.get("Page"))
    return render_template("list_posts.html",
                           database=pagination,
                           users=current_users,
                           image=image_source)

@post_manager.route('/<uuid:post_index>')
@setup_decorators.config_check
@inject_decorators.inject
def content(post_index,
            current: services.DATA_SOURCE_POSTS,
            image_source: services.DATA_SOURCE_IMAGES):

    return render_template("view_post.html",
                           current=current.get_by_id(post_index),
                           image=image_source)

@post_manager.route('/add', methods=["GET", "POST"])
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.requres_login
def add_item(current_database: services.DATA_SOURCE_POSTS,
             image_source: services.DATA_SOURCE_IMAGES):

    if request.method == "POST":
        to_add = BlogPost(
            request.form['NameInput'],
            session['logged_id'],
            request.form['ContentInput'],
            None)
        try:
            if 'image-file' in request.files:
                image_source.add_image(to_add, request.files['image-file'])
        except FileFormatException:
            flash('Illegal image type. No file uploaded')
        except FilePathException:
            pass

        current_database.add_post(to_add)
        return redirect(url_for('.content', post_index=to_add.post_id))
    return render_template("add_post.html")

@post_manager.route('/remove/<uuid:post_index>')
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.requres_login
@authorization_decorators.admin_or_owner_required
def remove_item(post_index, 
                current_database: services.DATA_SOURCE_POSTS, 
                image_source: services.DATA_SOURCE_IMAGES):

    to_be_removed=current_database.get_by_id(post_index)

    if to_be_removed.img_path is not None:
        image_source.remove_image(to_be_removed)

    current_database.remove(post_index)
    return redirect('/posts')

@post_manager.route('/update/<uuid:post_index>', methods=["GET", "POST"])
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.requres_login
@authorization_decorators.admin_or_owner_required
def update_item(post_index,
                current_database: services.DATA_SOURCE_POSTS,
                image_source: services.DATA_SOURCE_IMAGES):

    if request.method == "GET":
        return render_template("update_post.html",
                               current=current_database.get_by_id(post_index),
                               image=image_source)

    if request.method == "POST":
        current = current_database.get_by_id(post_index)

        if "update-post" in request.form:
            current.update(request.form['NameInput'],
                           request.form['ContentInput'],
                           current.img_path)
        try:
            if "remove-image" in request.form:
                image_source.remove_image(current)
        except FilePathException:
            flash("No image present. Nothing to remove")
            return redirect(url_for('.update_item', post_index=current.post_id))

        try:
            if "update-image" in request.form:
                if 'image-file' in request.files:
                    image_source.add_image(current, request.files['image-file'])
        except FileFormatException:
            flash("Invalid file type! Make sure a valid file format is selected")
            return redirect(url_for('.update_item', post_index=current.post_id))
        except FilePathException:
            flash("No image found. Provide a valid file")
            return redirect(url_for('.update_item', post_index=current.post_id))

        current_database.update_post(current)
        return redirect(url_for('.content', post_index=current.post_id))
    return Exception("Request type cannot be handled")

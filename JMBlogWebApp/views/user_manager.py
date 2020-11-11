from flask import Blueprint, render_template, request, redirect, url_for
from decorators import decorators
from setup import services_listing as services
from models.user import User

user_manager = Blueprint(
    'user_manager',
    __name__,
    url_prefix='/users',
    template_folder='templates')

@user_manager.route('/', methods=["GET"])
@decorators.config_check
@decorators.inject
def index(users_database: services.DATA_SOURCE_USERS):
    return render_template("list_users.html", database=users_database.get_users())

@user_manager.route('/<uuid:user_index>')
@decorators.config_check
@decorators.inject
def content(user_index, current: services.DATA_SOURCE_USERS):
    return render_template("view_user.html", element=current.get_user_by_id(user_index))

@user_manager.route('/add', methods=["GET", "POST"])
@decorators.config_check
@decorators.inject
def add_item(users_database: services.DATA_SOURCE_USERS):
    if request.method == "POST":
        to_add = User(
            request.form['NameInput'],
            request.form['EmailInput'],
            request.form['PasswordInput'])
        users_database.add_user(to_add)
        return redirect(url_for('.content', user_index=to_add.user_id))
    return render_template("add_user.html")

@user_manager.route('/remove/<uuid:user_index>')
@decorators.config_check
@decorators.inject
def remove_item(user_index, current_database: services.DATA_SOURCE_USERS):
    current_database.remove_user(user_index)
    return redirect('/users')

@user_manager.route('/update/<uuid:user_index>', methods=["GET", "POST"])
@decorators.config_check
@decorators.inject
def update_item(current_index, current_database: services.DATA_SOURCE_USERS):
    if request.method == "GET":
        return render_template("update_user.html",
                               current=current_database.get_by_id(current_index))

    if request.method == "POST":
        current = current_database.get_user_by_id(current_index)
        current.update(request.form['NameInput'],
                       request.form['EmailInput'],
                       request.form['PasswordInput'])
        current_database.update_post(current)
        return redirect(url_for('.content', current_index=current.post_id))
    return Exception("Request type cannot be handled")

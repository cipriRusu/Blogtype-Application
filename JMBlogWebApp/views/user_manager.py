from flask import Blueprint, render_template, request, redirect, url_for, flash
from setup import services_listing as services
from models.user import User
from views.decorators import setup_decorators
from views.decorators import inject_decorators
from views.decorators import authorization_decorators

user_manager = Blueprint(
    'user_manager',
    __name__,
    url_prefix='/users',
    template_folder='templates')

@user_manager.route('/', methods=["GET"])
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.admin_required
def index(current_database: services.DATA_SOURCE_USERS):
    return render_template("list_users.html", database=current_database.get_users())

@user_manager.route('/<uuid:user_index>')
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.admin_or_owner_required
def content(user_index, current_database: services.DATA_SOURCE_USERS):
    return render_template("view_user.html", element=current_database.get_user_by_id(user_index))

@user_manager.route('/add', methods=["GET", "POST"])
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.admin_required
def add_item(current_database: services.DATA_SOURCE_USERS):
    if request.method == "POST":
        to_add = User(
            request.form['NameInput'],
            request.form['EmailInput'],
            request.form['PasswordInput'])
        current_database.add_user(to_add)
        return redirect(url_for('.content', user_index=to_add.user_id))
    return render_template("add_user.html")

@user_manager.route('/remove/<uuid:user_index>')
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.admin_required
def remove_item(user_index, current_database: services.DATA_SOURCE_USERS):
    current_database.remove_user(user_index)
    return redirect('/users')

@user_manager.route('/update/<uuid:user_index>', methods=["GET", "POST"])
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.admin_or_owner_required
def update_item(user_index,
                current_database: services.DATA_SOURCE_USERS,
                login_manager: services.USER_LOGIN):
    if request.method == "GET":
        return render_template("update_user.html",
                               current=current_database.get_user_by_id(user_index))

    if request.method == "POST":
        current = current_database.get_user_by_id(user_index)
        current.update(request.form['UserNameInput'],
                       request.form['UserEmailInput'],
                       request.form['UserPassInput'])
        current_database.update_user(current)
        login_manager.login_update(current)
        return redirect(url_for('.content', user_index=current.user_id))
    return Exception("Request type cannot be handled")

@user_manager.route('/reset/<uuid:user_index>', methods=["GET", "POST"])
@setup_decorators.config_check
@inject_decorators.inject
@authorization_decorators.admin_or_owner_required
def reset_item(user_index,
               current_database: services.DATA_SOURCE_USERS,
               login_manager: services.USER_LOGIN):
    if request.method == "GET":
        return render_template("update_user.html",
                               current=current_database.get_user_by_id(user_index))

    if request.method == "POST":
        current = current_database.get_user_by_id(user_index)

        if not request.form['UserPassInput']:
            flash('Invalid password')
            return render_template("update_user.html",
                                   current=current_database.get_user_by_id(user_index))

        current.update(request.form['UserNameInput'],
                       request.form['UserEmailInput'],
                       request.form['UserPassInput'])
        login_manager.login_update(current)
        current_database.update_user(current)
        return redirect(url_for('user_manager.content', user_index=current.user_id))
    return Exception("Request type cannot be handled")

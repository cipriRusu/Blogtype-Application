from flask import Blueprint, render_template, request, redirect, url_for
from decorators import decorators
from setup import services_listing as services

user_manager = Blueprint(
    'user_manager',
    __name__,
    url_prefix='/users',
    template_folder='templates')

@user_manager.route('/', methods=["GET"])
@decorators.config_check
@decorators.inject
def index(current_database: services.DATA_SOURCE_USERS):
    return render_template("list_users.html", database=current_database.get_users())

@user_manager.route('/<uuid:current_index>')
@decorators.config_check
@decorators.inject
def content(current_index, current: services.DATA_SOURCE_USERS):
    return render_template("view_user.html", element=current.get_user_by_id(current_index))

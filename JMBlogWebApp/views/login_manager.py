from flask import Blueprint, render_template, request, redirect, url_for
from setup import services_listing as services
from decorators import decorators

login_manager = Blueprint('login_manager', __name__, url_prefix='/login',
                          template_folder='templates')

@login_manager.route('/', methods=["GET", "POST"])
@decorators.config_check
@decorators.inject
def login(login_service: services.USER_LOGIN):
    if request.method == "POST":
        login_service.get_credentials(
            request.form['NameInput'],
            request.form['PasswordInput'])
        #TODO: Implement login validation & session
        login_service.is_login_valid()
        return redirect(url_for('post_manager.index'))
    return render_template("login_user.html")

from flask import Blueprint, render_template, request, redirect, url_for
from setup import services_listing as services
from decorators import decorators

login_manager = Blueprint('login_manager', __name__, url_prefix='/authentication',
                          template_folder='templates')

@login_manager.route('/login', methods=["GET", "POST"])
@decorators.config_check
@decorators.inject
def login(login_service: services.USER_LOGIN):
    if request.method == "POST":
        if login_service.user_login(request.form['NameInput'],
                                    request.form['PasswordInput']) is True:
            return redirect(url_for("post_manager.index"))
        return render_template("login_user.html")
    return render_template("login_user.html")

@login_manager.route('/logout', methods=["GET"])
@decorators.config_check
@decorators.inject
def logout(login_service: services.USER_LOGIN):
    login_service.user_logout()
    return render_template("login_user.html")

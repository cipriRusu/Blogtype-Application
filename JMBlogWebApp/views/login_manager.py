from flask import Blueprint, render_template, request, redirect, url_for, session
from decorators import decorators

login_manager = Blueprint(
    'login_manager',
    __name__,
    url_prefix='/login',
    template_folder='templates')

@login_manager.route('/', methods=["GET", "POST"])
@decorators.config_check
@decorators.inject
def login():
    #TODO: Inject login manager?
    if request.method == "POST":
        session['logged'] = request.form['NameInput']
        return redirect(url_for('post_manager.index'))
    return render_template("login_user.html")

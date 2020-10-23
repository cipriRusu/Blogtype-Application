from flask import Blueprint, render_template, request, redirect, url_for
from services.services import Services

setup_manager = Blueprint(
    'connection_manager',
    __name__,
    url_prefix='/setup',
    template_folder='templates')

@setup_manager.route('/', methods=["GET", "POST"])
def database_connector():
    if request.method == "GET":
        if Services().get_service('config').is_configured() or Services().IS_TEST:
            Services().get_service('connect')
            return redirect(url_for('post_manager.index'))
        return render_template("setup.html")
    if request.method == "POST":
        Services().get_service('config').to_file(request.form, 'db_connection')
        Services().get_service('connect')
        return redirect(url_for('post_manager.index'))
    return Exception("Cannot handle current request")

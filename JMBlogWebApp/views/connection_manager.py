from flask import Blueprint, render_template, request, redirect, url_for

connection_manager = Blueprint(
    'connection_manager',
    __name__,
    url_prefix='/dbsetup',
    template_folder='templates')

@connection_manager.route('/', methods=["GET", "POST"])
def database_connector():
    if request.method == "GET":
        return render_template("conn_config_db.html")

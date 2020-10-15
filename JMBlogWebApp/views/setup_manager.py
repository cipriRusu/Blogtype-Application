from flask import Blueprint, render_template, request, redirect, url_for
from setup.db_setup import DbSetup
from setup.config import Config

setup_manager = Blueprint(
    'connection_manager',
    __name__,
    url_prefix='/setup',
    template_folder='templates')

@setup_manager.route('/', methods=["GET", "POST"])
def database_connector():
    if request.method == "GET":
        return render_template("setup.html")
    if request.method == "POST":
        Config().to_file(request.form, 'db_connection')
        DbSetup(
            {'host': request.form['host'],
             'user': request.form['user'],
             'password': request.form['password'],
             'database' : request.form['database']})

        return redirect(url_for('post_manager.index'))
    return Exception("Cannot handle current request")

from flask import Blueprint, render_template, request, redirect, url_for
from setup import services_listing as services
from setup.config import Config
from setup.db_setup import DbSetup
from services.services import Services
from decorators import decorators

setup_manager = Blueprint(
    'setup_manager',
    __name__,
    url_prefix='/setup',
    template_folder='templates')

@setup_manager.route('/', methods=["GET", "POST"])
@decorators.inject
def database_connector(current_config: "Config", current_setup: "DbSetup"):
    if request.method == "GET":
        if current_config.is_configured():
            return redirect(url_for('post_manager.index'))
        return render_template("setup.html")

    if request.method == "POST":
        current_config.to_file(request.form, 'db_connection')
        current_setup.create_database()
        return redirect(url_for('post_manager.index'))
    return Exception("Cannot handle current request")

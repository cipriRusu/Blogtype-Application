from decorators import decorators
from flask import Blueprint, render_template, request, redirect, url_for
from models.database_configuration import DatabaseConfiguration
from setup import services_listing as services

setup_manager = Blueprint(
    'setup_manager',
    __name__,
    url_prefix='/setup',
    template_folder='templates')

@setup_manager.route('/', methods=["GET", "POST"])
@decorators.inject
def database_connector(current_db_config: services.DB_CONFIGURATION, setup: services.SETUP):
    if request.method == "GET":
        if current_db_config.is_configured():
            return redirect(url_for('post_manager.index'))
        return render_template("setup.html")

    if request.method == "POST":
        current_db_config.save_configuration(DatabaseConfiguration(**request.form))
        setup.create_database()
        return redirect(url_for('post_manager.index'))
    return Exception("Cannot handle current request")

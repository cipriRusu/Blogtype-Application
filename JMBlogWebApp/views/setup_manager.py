from flask import Blueprint, render_template, request, redirect, url_for
from setup import services_listing as services
from services.services import Services

setup_manager = Blueprint(
    'connection_manager',
    __name__,
    url_prefix='/setup',
    template_folder='templates')

@setup_manager.route('/', methods=["GET", "POST"])
def database_connector():
    current_config = Services.get_service(services.CONFIGURE)
    current_setup = Services.get_service(services.SETUP)

    if request.method == "GET":
        if current_config.is_configured():
            return redirect(url_for('post_manager.index'))
        return render_template("setup.html")

    if request.method == "POST":
        current_config.to_file(request.form, 'db_connection')
        current_setup.create_database()
        return redirect(url_for('post_manager.index'))
    return Exception("Cannot handle current request")

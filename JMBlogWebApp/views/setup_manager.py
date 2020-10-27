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
    if request.method == "GET":
        if Services.get_service(services.CONFIGURE).is_configured():
            return redirect(url_for('post_manager.index'))
        return render_template("setup.html")

    if request.method == "POST":
        #save configuration to file
        Services.get_service(services.CONFIGURE).to_file(request.form, 'db_connection')

        #get current configuration
        config = Services.get_service(services.CONFIGURE).from_file('db_connection')

        #connect to database server
        Services.get_service(services.SETUP).get_connection(**config)

        #create database and posts table
        Services.get_service(services.SETUP).create_database()

        #link data source to current database
        Services.get_service(services.DATA_SOURCE).get_parameters(**config)

        return redirect(url_for('post_manager.index'))
    return Exception("Cannot handle current request")

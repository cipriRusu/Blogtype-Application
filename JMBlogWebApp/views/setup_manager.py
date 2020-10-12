import configparser
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
    if request.method == "POST":
        config = configparser.ConfigParser()
        config['postgresql_conn_data'] = { 'host' : request.form['HostInput'],
                                           'dbname' : request.form['DatabaseInput'],
                                           'port' : request.form['PortInput'],
                                           'user' : request.form['UsernameInput'],
                                           'password' : request.form['PasswordInput']}

        with open('./setup/database.ini', 'w') as configfile:
            config.write(configfile)

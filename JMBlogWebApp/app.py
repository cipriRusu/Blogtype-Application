import os
from flask import Flask, redirect
from views import post_manager
from views import setup_manager
from views import user_manager
from views import login_manager
from views import error_manager
from views.decorators import inject_decorators
from setup import services_listing as services

app = Flask(__name__, static_url_path="", static_folder="static")
app.secret_key = os.urandom(10)

with app.app_context():
    app.register_blueprint(post_manager.post_manager)
    app.register_blueprint(setup_manager.setup_manager)
    app.register_blueprint(user_manager.user_manager)
    app.register_blueprint(login_manager.login_manager)
    app.register_blueprint(error_manager.error_manager)

    @app.before_first_request
    @inject_decorators.inject
    def check_db_version(db_version: services.DB_VERSION):
        CURRENT_VERSION = 0
        if db_version.is_configured():
            CURRENT_VERSION = db_version.load_configuration()['version']

    @app.route('/')
    @app.route('/<path:path>')
    def catch_all():
        return redirect('/setup', 302)

if __name__ == '__main__':
    app.run('localhost', 4449)

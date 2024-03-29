import os
from flask import Flask, redirect
from views import post_manager
from views import setup_manager
from views import user_manager
from views import login_manager
from views import error_manager
from views import statistics_manager
from views import api_manager
from views.decorators import inject_decorators
from setup import services_listing as services

app = Flask(__name__, static_url_path="", static_folder="static")
app.secret_key = os.urandom(10)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['LOGIN_KEY'] = 'N\x0f\x95\xa7\x0c:Pt\xfaZ'

with app.app_context():
    app.register_blueprint(post_manager.post_manager)
    app.register_blueprint(setup_manager.setup_manager)
    app.register_blueprint(user_manager.user_manager)
    app.register_blueprint(login_manager.login_manager)
    app.register_blueprint(error_manager.error_manager)
    app.register_blueprint(statistics_manager.stat_manager)
    app.register_blueprint(api_manager.api_manager)

    @app.before_first_request
    @inject_decorators.inject
    def before_first_request(setup: services.SETUP):
        if setup.is_db_outdated():
            setup.setup()

    @app.route('/')
    @app.route('/<path:path>')
    def catch_all():
        return redirect('/setup', 302)

if __name__ == '__main__':
    app.run('localhost', 4449)

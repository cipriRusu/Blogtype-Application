from functools import wraps
from flask import redirect, url_for, session, render_template
from setup import services_listing as services
from services.services import Services

current_db_config = Services.get_service(services.DB_CONFIGURATION)

def config_check(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if current_db_config.is_configured():
            return function(*args, **kwargs)
        return redirect(url_for('setup_manager.database_connector'))
    return wrapper

def inject(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for element in func.__annotations__.items():
            kwargs[element[0]] = (Services.get_service(element[1]) if
                                  Services.is_service(element[1]) else element[1])
        return func(*args, **kwargs)
    return wrapper

def requires_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_name' in session:
            if session['logged_name'] == 'admin':
                return func(*args, **kwargs)
        return render_template("unauthorized.html")
    return wrapper

def requres_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_name' in session:
            return func(*args, **kwargs)
        return render_template("unauthorized.html")
    return wrapper

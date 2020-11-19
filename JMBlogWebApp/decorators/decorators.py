from functools import wraps
from flask import redirect, url_for, session
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
        return redirect(url_for('error_manager.error_redirect'))
    return wrapper

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_name' in session:
            return func(*args, **kwargs)
        return redirect(url_for('error_manager.error_redirect'))
    return wrapper

def admin_or_owner_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'post_index' in kwargs:
            found_post = kwargs['current_database'].get_by_id(kwargs['post_index'])
            if 'logged_name' in session:
                if found_post.author == session['logged_name'] or session['logged_name'] == 'admin':
                    return func(*args, **kwargs)
            return redirect(url_for('error_manager.error_redirect'))

        if 'user_index' in kwargs:
            found_user = kwargs['current_database'].get_user_by_id(kwargs['user_index'])
            if 'logged_name' in session:
                if found_user.user_name == session['logged_name'] or session['logged_name'] == 'admin':
                    return func(*args, **kwargs)
                return redirect(url_for('error_manager.error_redirect'))
            return redirect(url_for('error_manager.error_redirect'))
    return wrapper

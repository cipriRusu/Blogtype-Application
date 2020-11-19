from functools import wraps
from flask import redirect, url_for
from services.services import Services

current_config = Services.db_configuration

def config_check(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if current_config.is_configured():
            return function(*args, **kwargs)
        return redirect(url_for('setup_manager.database_connector'))
    return wrapper

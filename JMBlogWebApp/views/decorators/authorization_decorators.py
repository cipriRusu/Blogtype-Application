from functools import wraps
from flask import redirect, url_for, session

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_name' in session:
            if session['logged_name'] == 'admin':
                return func(*args, **kwargs)
            return redirect(url_for('error_manager.error_redirect'))
        return redirect(url_for('error_manager.error_redirect'))
    return wrapper

def requres_login(func):
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
                if (found_post.author == session['logged_name'] or
                        session['logged_name'] == 'admin'):
                    return func(*args, **kwargs)
                return redirect(url_for('error_manager.error_redirect'))
            return redirect(url_for('error_manager.error_redirect'))

        if 'user_index' in kwargs:
            found_user = kwargs['current_database'].get_user_by_id(kwargs['user_index'])
            if 'logged_name' in session:
                if (found_user.user_name == session['logged_name'] or
                        session['logged_name'] == 'admin'):
                    return func(*args, **kwargs)
                return redirect(url_for('error_manager.error_redirect'))
            return redirect(url_for('error_manager.error_redirect'))
    return wrapper

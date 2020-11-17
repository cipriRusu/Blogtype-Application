from flask import Blueprint, render_template, request, redirect, url_for

error_manager = Blueprint(
    'error_manager',
    __name__,
    url_prefix='/error',
    template_folder='templates')

@error_manager.route('/', methods=["GET", "POST"])
def error_redirect():
    if request.method == "POST":
        return redirect(url_for('post_manager.index'))
    return render_template("unauthorized.html")

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from setup import services_listing as services
from views.decorators import setup_decorators
from views.decorators import inject_decorators

stat_manager = Blueprint('statistics_manager',__name__,url_prefix='/user_statistics', template_folder='templates')

@stat_manager.route('/', methods=["GET"])
@setup_decorators.config_check
@inject_decorators.inject
def user_statistics():
    return render_template('user_statistics.html')

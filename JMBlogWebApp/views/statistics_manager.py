from flask import Blueprint, render_template, request
from setup import services_listing as services
from views.decorators import setup_decorators
from views.decorators import inject_decorators

stat_manager = Blueprint('statistics_manager',
                         __name__,
                         url_prefix='/user_statistics',
                         template_folder='templates')

@stat_manager.route('/', methods=["GET"])
@setup_decorators.config_check
@inject_decorators.inject
def user_statistics(user_stats: services.USER_STATISTICS,
                    current_users: services.DATA_SOURCE_USERS):
    user_stats = user_stats.get_statistics(request.args.get("Users"))
    return render_template('user_statistics.html', users=current_users, stats=user_stats)

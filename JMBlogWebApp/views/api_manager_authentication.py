from flask import Blueprint, jsonify, request
from views.decorators import setup_decorators
from views.decorators import inject_decorators
from setup import services_listing as services

api_manager_authentication = Blueprint('api_manager_authentication', __name__,
                                       url_prefix='/api/authentication',
                                       template_folder='templates',
                                       static_folder='static')

@api_manager_authentication.route('/login', methods=["POST"])
@setup_decorators.config_check
@inject_decorators.inject
def login(auth_manager: services.USER_LOGIN,
          users: services.DATA_SOURCE_USERS,
          token_manager: services.TOKEN_HANDLING):

    if auth_manager.user_login(request.authorization.username,
                               request.authorization.password):

        found_user = users.get_by_name(request.authorization.username)
        generated_token = token_manager.create_token(found_user)
        return jsonify({'token': generated_token.decode()})
    return jsonify({'token' : 'authorization failed'}), 403

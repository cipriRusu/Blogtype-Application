from flask import Blueprint, jsonify, request
from views.decorators import setup_decorators
from views.decorators import inject_decorators
from views.decorators import token_decorators
from setup import services_listing as services

api_manager = Blueprint('api_manager', __name__, url_prefix='/api',
                        template_folder='templates',
                        static_folder='static')

@api_manager.route('/posts/<uuid:post_index>', methods=["GET"])
@setup_decorators.config_check
@inject_decorators.inject
def get_item(post_index,
             current: services.DATA_SOURCE_POSTS):
    post = current.get_by_id(post_index)
    return jsonify(post.to_dict())

@api_manager.route('/posts/remove/<uuid:post_index>')
@setup_decorators.config_check
@inject_decorators.inject
@token_decorators.token_required
def remove_item(post_index, posts: services.DATA_SOURCE_POSTS):
    posts.remove(post_index)
    return jsonify({'message' : 'Post was deleted successfully!'})

@api_manager.route('/login', methods=["POST"])
@setup_decorators.config_check
@inject_decorators.inject
def login(auth_manager: services.USER_LOGIN,
          users: services.DATA_SOURCE_USERS,
          token_manager: services.TOKEN_HANDLING):

    if auth_manager.user_login(request.authorization.username,
                               request.authorization.password):

        found_user = users.get_by_name(request.authorization.username)
        generated_token = token_manager.create_token(found_user)
        return jsonify({'token': generated_token})
    return jsonify({'token' : 'authorization failed'})

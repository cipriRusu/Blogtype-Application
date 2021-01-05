import datetime
import jwt
from flask import Blueprint, jsonify, request, current_app
from views.decorators import setup_decorators
from views.decorators import inject_decorators
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
def remove_item(post_index, posts: services.DATA_SOURCE_POSTS):
    token = None

    if 'x-access-token' in request.headers:

        token = request.headers['x-access-token']

        data = jwt.decode(token, current_app.secret_key, algorithms=["HS256"])

    return jsonify({'message' : 'Post was deleted successfully!'})

@api_manager.route('/login', methods=["POST"])
@setup_decorators.config_check
@inject_decorators.inject
def login(users: services.DATA_SOURCE_USERS):
    auth = request.authorization

    user = users.get_by_name(auth.username)

    token = jwt.encode({'user_id': user.user_id.hex,
                        'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=1)},
                       current_app.secret_key)

    return jsonify({'token' : token})

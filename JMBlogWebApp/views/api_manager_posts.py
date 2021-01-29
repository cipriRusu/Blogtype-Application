from exceptions.post_not_found_exception import PostNotFoundException
from flask import Blueprint, jsonify
from views.decorators import setup_decorators
from views.decorators import inject_decorators
from views.decorators import token_decorators
from setup import services_listing as services

api_manager_posts = Blueprint('api_manager_posts', __name__,
                              url_prefix='/api/posts/',
                              template_folder='templates',
                              static_folder='static')

@api_manager_posts.route('/', methods=["GET"])
@setup_decorators.config_check
@inject_decorators.inject
def get_all(posts: services.DATA_SOURCE_POSTS):
    return jsonify([item.to_dict() for item in posts.get_all()])

@api_manager_posts.route('/<uuid:post_index>', methods=["GET"])
@setup_decorators.config_check
@inject_decorators.inject
def get_item(post_index,
             current: services.DATA_SOURCE_POSTS):
    try:
        post = current.get_by_id(post_index)
    except PostNotFoundException:
        return jsonify({"message": "Resource not available"}), 404
    return jsonify(post.to_dict())

@api_manager_posts.route('/remove/<uuid:post_index>')
@setup_decorators.config_check
@inject_decorators.inject
@token_decorators.token_required
def remove_item(post_index, posts: services.DATA_SOURCE_POSTS):
    posts.remove(post_index)
    return jsonify({'message' : 'Post was deleted successfully!'})

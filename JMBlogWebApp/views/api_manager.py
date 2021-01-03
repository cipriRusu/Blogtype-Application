from flask import Blueprint, jsonify
from views.decorators import setup_decorators
from views.decorators import inject_decorators
from setup import services_listing as services

api_manager = Blueprint('api_manager', __name__, url_prefix='/api/posts',
                        template_folder='templates',
                        static_folder='static')

@api_manager.route('/<uuid:post_index>', methods=["GET"])
@setup_decorators.config_check
@inject_decorators.inject
def get_item(post_index,
             current: services.DATA_SOURCE_POSTS):
    post = current.get_by_id(post_index)
    return jsonify(post.to_dict())

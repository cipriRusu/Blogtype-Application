from functools import wraps
from exceptions.postnotfound_exception import PostNotFoundException
import jwt
from flask import request, jsonify, current_app

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if "Authorization" not in request.headers:
            return jsonify({'message': 'Post removing failed!'})

        token_string = request.headers['Authorization'][7:]

        try:
            data = jwt.decode(token_string,
                              current_app.config['LOGIN_KEY'],
                              algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired, please login again'})

        try:
            if 'posts' in kwargs:
                current_post = kwargs['posts'].get_by_id(kwargs['post_index'])

            if data['user_name'] != 'admin' and data['user_name'] != current_post.author:
                return jsonify({'message': 'Unauthorized operation!'})
        except PostNotFoundException:
            return jsonify({'message': 'Post already removed!'})

        return func(*args, **kwargs)
    return wrapper

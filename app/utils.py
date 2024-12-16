from flask import jsonify
from functools import wraps
from flask_jwt_extended import get_jwt, jwt_required


def roles_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get("role")

            if user_role not in allowed_roles:
                return jsonify({"msg": "Access forbidden: insufficient permissions"}), 403

            return func(*args, **kwargs)

        return wrapper
    return decorator

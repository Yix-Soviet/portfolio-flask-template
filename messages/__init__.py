from flask import Blueprint

from .api.resource import hello_world, get_messages, create_message

def create_resources():
    messsages_bp = Blueprint('messages', __name__, url_prefix="/messages")
    messsages_bp.add_url_rule('/hello-world', view_func=hello_world, methods=["GET"])
    messsages_bp.add_url_rule('', view_func=get_messages, methods=["GET"])
    messsages_bp.add_url_rule('/create', view_func=create_message, methods=["POST"])

    return messsages_bp
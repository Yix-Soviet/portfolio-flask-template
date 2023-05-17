from flask import Blueprint

from .api.resource import hello_world

def create_resources():
    projects_bp = Blueprint('projects', __name__, url_prefix="/projects")
    projects_bp.add_url_rule('/hello-world', view_func=hello_world)

    return projects_bp
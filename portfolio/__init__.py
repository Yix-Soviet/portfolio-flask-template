from flask import Blueprint

from .app.resource import presentation_card, portfolio_web


def create_resources(subdomain: bool) -> Blueprint:
    if subdomain == False:
        presentation_bp = Blueprint('presentation_card', __name__, url_prefix="/", template_folder="templates", static_folder="static", static_url_path="portfolio/static")
        presentation_bp.add_url_rule('', view_func=presentation_card, methods=["GET"])

        return presentation_bp
    else:
        portfolio_bp = Blueprint('portfolio_web', __name__, url_prefix="/", template_folder="templates", static_folder="static", static_url_path="portfolio/static")
        portfolio_bp.add_url_rule('', view_func=portfolio_web, methods=["GET"])

        return portfolio_bp

from flask import Blueprint
from .email_view import EmailView

email_view = EmailView()

blueprint = Blueprint("views", __name__, template_folder="templates")

blueprint.add_url_rule("/", view_func=email_view.index, methods=["GET", "POST"])


def init(app):
    app.register_blueprint(blueprint)

from flask import request, Blueprint
import json

health_blueprint = Blueprint('health_blueprint', __name__)

@health_blueprint.route("/")
def health():
    return ('', 204)
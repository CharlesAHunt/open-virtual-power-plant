from flask import request, Blueprint
from ovpp.service.der import createDER
import json


der_blueprint = Blueprint('der_blueprint', __name__)


@der_blueprint.route("/der", methods=["GET", "POST"])
def get_all_ders():
    if request.method == 'GET':
        der = createDER()
        return json.dumps(der, default=lambda der: der.__dict__)
    elif request.method == 'POST':
        return ('', 204)
    elif request.method == 'PUT':
        return ('', 204)
    else:
        return ('', 405)

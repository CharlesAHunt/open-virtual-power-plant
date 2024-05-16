from flask import Flask
from ovpp.models.der import DER
import json

app = Flask(__name__)

@app.route("/")
def health():
    return ('', 204)

@app.route("/der")
def ders():
    der = DER("name", "type", "capacity", "cost")
    return json.dumps(der, default=lambda der: der.__dict__)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
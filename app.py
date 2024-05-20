from flask import Flask
from ovpp.routes import der, health
import psycopg2
import tomllib

with open("config.toml", mode="rb") as fp:
    configDict = tomllib.load(fp)
    conn = psycopg2.connect(database=configDict["database"]["database"],
                            host=configDict["database"]["host"],
                            user=configDict["database"]["user"],
                            password=configDict["database"]["password"],
                            port=configDict["database"]["port"])

app = Flask(__name__)

app.register_blueprint(der.der_blueprint)
app.register_blueprint(health.health_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
from config import load_config
from connect import connect
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def create_app():
    config = load_config()
    db_connection = connect(config)
    return db_connection


if __name__ == "__main__":
    app.run(debug=True)

from db.db import PostgreSQLConnection
from flask import Flask, jsonify
from flask_cors import CORS
from routes.authors import authors

app = Flask(__name__)
app.register_blueprint(authors)
CORS(app)
db = PostgreSQLConnection()


@app.route("/")
def index():
    result = db.execute_query("SELECT * FROM author", ())
    return jsonify([row for row in result])


if __name__ == "__main__":
    app.run(debug=True)

# TODO: Add rest of the models Active Record
# TODO: Add API endpoints using Blueprint
# TODO: Add error handling
# TODO: Add authentication

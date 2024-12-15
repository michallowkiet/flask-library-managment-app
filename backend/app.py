from flask import Flask, jsonify
from flask_cors import CORS
from models.author import Author
from postgresql_connection import PostgreSQLConnection

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    author = Author(
        "John Doe",
        PostgreSQLConnection(),
    )

    try:
        author.save()
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({"Author ID": author.id})


if __name__ == "__main__":
    app.run(debug=True)

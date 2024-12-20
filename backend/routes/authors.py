from db.db import PostgreSQLConnection
from flask import Blueprint, jsonify, request
from models.author import Author

authors = Blueprint("authors", __name__)
db_connection = PostgreSQLConnection()


@authors.route("/authors", methods=["GET"])
def get_authors():
    return Author.all(db_connection)


@authors.route("/authors/<name>", methods=["GET"])
def get_author_by_name(name):
    author = Author.find_by_author_name(name, db_connection)
    if author:
        return jsonify(author)
    return jsonify({"error": "Author not found"}), 404


@authors.route("/authors", methods=["POST"])
def create_author():
    if request.method == "POST":
        author = Author(request.json["name"])
        author.save(db_connection)

        return jsonify(author.to_dict()), 201


@authors.route("/authors", methods=["DELETE"])
def delete_author():
    if request.method == "DELETE":
        author = Author.find_by_id(request.json["id"], db_connection)

        if author:
            author.delete(db_connection)
            return jsonify({"message": f"Author {author.name} deleted"}), 200

        return jsonify({"error": "Author not found"}), 404

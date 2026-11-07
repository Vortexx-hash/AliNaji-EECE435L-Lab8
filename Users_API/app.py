"""Lab 8 - small Flask API exposing GET /get_users on port 3000."""
from flask import Flask, jsonify

import database

app = Flask(__name__)
database.create_db_table()


@app.route("/get_users", methods=["GET"])
def get_users():
    """Return the list of the names of all users in the database."""
    return jsonify([user["name"] for user in database.get_users()])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

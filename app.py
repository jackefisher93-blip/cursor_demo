from flask import Flask, request, jsonify
from db import get_user, create_user, get_all_users
from auth import validate_token

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def users():
    token = request.headers.get("Authorization")
    if not validate_token(token):
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify(get_all_users())

@app.route("/users", methods=["POST"])
def create():
    data = request.json
    user = create_user(data["name"], data["email"])
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(debug=True)


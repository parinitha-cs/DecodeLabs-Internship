from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Aisha",
        "email": "aisha@example.com"
    },
    {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to REST API Fundamentals"
    })


@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({
        "success": True,
        "users": users
    })


@app.route("/api/users", methods=["POST"])
def add_user():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No JSON data provided"
        }), 400

    if "name" not in data or "email" not in data:
        return jsonify({
            "success": False,
            "message": "Name and email are required"
        }), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)

    return jsonify({
        "success": True,
        "message": "User created successfully",
        "user": new_user
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
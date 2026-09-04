from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import sqlite3
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from functools import wraps


load_dotenv()


app = Flask(__name__)


SECRET_KEY = os.getenv("JWT_SECRET", "temporary-secret-key")

app.config["SECRET_KEY"] = SECRET_KEY




def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()



init_db()




@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Request body is required"
        }), 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({
            "message": "Username, email and password are required"
        }), 400

    
    hashed_password = generate_password_hash(password)

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
            """,
            (username, email, hashed_password)
        )

        conn.commit()
        conn.close()

        return jsonify({
            "message": "User registered successfully"
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({
            "message": "Email already registered"
        }), 409




@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Request body is required"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and password are required"
        }), 400

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, username, password
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    user_id, username, hashed_password = user

    
    if not check_password_hash(hashed_password, password):
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    
    token = jwt.encode(
        {
            "user_id": user_id,
            "username": username,
            "exp": datetime.now(timezone.utc) + timedelta(hours=1)
        },
        SECRET_KEY,
        algorithm="HS256"
    )

    return jsonify({
        "message": "Login successful",
        "token": token
    }), 200




def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        
        auth_header = request.headers.get("Authorization")

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ", 1)[1]

        
        if not token:
            return jsonify({
                "message": "Token is missing"
            }), 401

        try:
            
            decoded = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"]
            )

            
            request.user = decoded

        except jwt.ExpiredSignatureError:
            return jsonify({
                "message": "Token has expired"
            }), 401

        except jwt.InvalidTokenError:
            return jsonify({
                "message": "Invalid token"
            }), 401

        return f(*args, **kwargs)

    return decorated




@app.route("/protected", methods=["GET"])
@token_required
def protected():

    return jsonify({
        "message": "You have accessed a protected route",
        "user": request.user
    }), 200




@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Secure Authentication API is running"
    }), 200



if __name__ == "__main__":
    app.run(debug=True)
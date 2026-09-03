# DecodeLabs Backend Development Internship
## Project 2 – Database Integration (CRUD)

### Project Overview

This project was developed as part of the DecodeLabs Backend Development Internship.

The objective of Project 2 is to integrate a backend REST API with a database so that user information can be stored persistently instead of being maintained only in temporary memory.

The application implements complete CRUD operations for user data and includes validation to prevent duplicate email entries.

---

## Objectives

- Connect a Flask REST API with a database.
- Design and implement a simple User schema.
- Implement Create, Read, Update, and Delete operations.
- Store user information persistently.
- Prevent duplicate user entries using unique email validation.
- Use an ORM for database interaction.

---

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy ORM
- SQLite
- REST API
- Postman for API testing

---

## User Schema

The application uses the following User model:

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Primary key |
| `name` | String | User's name |
| `email` | String | User's email address |

The email field is configured as unique to prevent duplicate user records.

---

## CRUD API Endpoints

### 1. Create User

**Endpoint:**

`POST /api/users`

Creates a new user in the database.

**Request Body:**

```json
{
    "name": "John",
    "email": "john@example.com"
}

2. Get All Users

Endpoint:

GET /api/users

Returns all users stored in the database.

3. Get User by ID

Endpoint:

GET /api/users/<user_id>

Returns the details of a specific user.

4. Update User

Endpoint:

PUT /api/users/<user_id>

Updates the name or email of an existing user.

Request Body:

{
    "name": "John Updated",
    "email": "john.updated@example.com"
}

5. Delete User

Endpoint:

DELETE /api/users/<user_id>

Deletes an existing user from the database.

Duplicate Entry Prevention

The application prevents duplicate email addresses.

If a user attempts to register with an email address that already exists, the API returns:

HTTP Status: 409 Conflict

{
    "error": "Email already exists"
}

This ensures that duplicate user records are not stored in the database.

Database Integration

The project uses SQLite as the database and Flask-SQLAlchemy as the ORM.

SQLAlchemy allows the application to interact with the database using Python objects and models instead of writing raw SQL queries for every database operation.

Project Structure
Project-2/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
Installation and Setup
1. Create a Virtual Environment
python -m venv venv
2. Activate the Virtual Environment

Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
python app.py
API Testing

The REST API was tested using Postman.

The following operations were tested:

Create User
Get All Users
Get User by ID
Update User
Delete User
Duplicate Email Validation

The API returned appropriate HTTP status codes for successful operations, validation errors, and duplicate entries.

Key Features
RESTful API architecture
Persistent database storage
Complete CRUD functionality
SQLAlchemy ORM integration
User input validation
Duplicate email prevention
Appropriate HTTP status codes
Simple and maintainable implementation
Learning Outcomes

Through this project, I gained practical experience in:

Database integration with Flask
SQLAlchemy ORM
REST API development
CRUD operations
Data validation
Persistent data storage
API testing using Postman
Author

Parinitha CS

DecodeLabs Backend Development Internship – 2026
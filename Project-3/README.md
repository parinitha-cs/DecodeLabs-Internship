# Project 3 – Secure Authentication API

## Overview

This project implements a secure user authentication REST API using Flask and SQLite. It provides user registration, login, password hashing, and JWT-based authentication for protected routes.

## Features

* User registration
* Secure password hashing
* User login and password verification
* JWT token generation
* Protected API route
* JWT token validation
* Token expiration handling
* Invalid token handling
* SQLite database integration

## Technologies Used

* Python
* Flask
* SQLite
* PyJWT
* Werkzeug
* python-dotenv
* Postman

## Project Structure

```text
Project-3/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## API Endpoints

| Method | Endpoint     | Description                                      |
| ------ | ------------ | ------------------------------------------------ |
| POST   | `/register`  | Register a new user                              |
| POST   | `/login`     | Authenticate a user and generate a JWT token     |
| GET    | `/protected` | Access a protected route using a valid JWT token |
| GET    | `/`          | Check whether the API is running                 |

## Registration

Send a POST request to:

```text
/register
```

Example request:

```json
{
    "username": "testuser",
    "email": "test@gmail.com",
    "password": "Test@123"
}
```

## Login

Send a POST request to:

```text
/login
```

Example request:

```json
{
    "email": "test@gmail.com",
    "password": "Test@123"
}
```

A successful login returns a JWT token.

## Protected Route

Send a GET request to:

```text
/protected
```

Use the JWT token received from the login request as a Bearer Token in the Authorization header.

A valid token allows access to the protected route.

## Authentication Testing

The API was tested using Postman for:

* Successful registration
* Successful login
* Valid JWT token
* Missing JWT token
* Invalid JWT token

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Application

Run:

```bash
python app.py
```

The API will start locally at:

```text
http://127.0.0.1:5000
```

## Security

Sensitive configuration such as environment variables and the local SQLite database should not be committed to the repository. These files are excluded using `.gitignore`.

## Author

Internship Project – Project 3

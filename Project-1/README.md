# DecodeLabs Backend Development Internship
## Project 1 — REST API Fundamentals

### 📌 Project Overview

This project is part of the DecodeLabs Backend Development Internship.

Project 1 focuses on the fundamentals of REST API development. The objective is to build a local, stateless web server that handles HTTP requests through defined routes and returns structured JSON responses.

The project demonstrates the basic communication layer between a client and a backend server using REST principles.

---

## 🎯 Objectives

The main objectives of this project are:

- Create and run a local backend server
- Understand HTTP methods
- Implement GET and POST routes
- Implement routing logic
- Return structured JSON responses
- Handle client-provided JSON data
- Validate incoming data
- Use appropriate HTTP status codes
- Test REST API endpoints using Postman

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **REST API**
- **JSON**
- **Postman**
- **Git & GitHub**

---

## ✨ Features

### 1. Local Web Server
A Flask-based local server is created to handle API requests.

### 2. GET API
The application provides GET endpoints to retrieve information from the server.

### 3. POST API
The application provides a POST endpoint that accepts JSON data and creates a new user.

### 4. JSON Responses
All API responses are returned in structured JSON format.

### 5. Input Validation
The POST endpoint checks whether the required `name` and `email` fields are provided.

### 6. HTTP Status Codes
The API uses appropriate status codes such as:

- `200` — Successful request
- `201` — User successfully created
- `400` — Invalid or missing input

---

## 📂 Project Structure

```text
Decodelabs-Internship/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

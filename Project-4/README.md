# Backend Development Project 4 – Third-Party API Integration

## Project Overview

This project demonstrates how to integrate a third-party Weather API with a Flask backend application.

The application accepts a city name, fetches weather information from the OpenWeather API, processes the external response, and returns a simplified JSON response to the user.

## Objectives

* Integrate a third-party API with a backend application.
* Securely manage the external API key using environment variables.
* Fetch external API data asynchronously.
* Reformat external API data into a simple JSON response.
* Handle API and connection errors properly.
* Test the backend API using Postman.

## Technologies Used

* Python
* Flask
* aiohttp
* python-dotenv
* OpenWeather API
* Postman
* Git and GitHub

## Project Structure

```text
Project-4/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── venv/
```

> `.env` and `venv/` are excluded from GitHub using `.gitignore`.

## API Endpoint

### Get Weather Information

**Method:** `GET`

**Endpoint:**

```text
/weather/<city>
```

**Example:**

```text
http://127.0.0.1:5000/weather/Bengaluru
```

## Example Successful Response

```json
{
    "city": "Bengaluru",
    "country": "IN",
    "feels_like": 26.15,
    "humidity": 70,
    "temperature": 26.15,
    "weather": "overcast clouds",
    "wind_speed": 4.98
}
```

The weather values are live data and may change between requests.

## Error Handling

If an invalid city is provided, the API returns a `404 Not Found` response:

```json
{
    "error": "City not found"
}
```

The application also handles timeout and connection errors when communicating with the external weather service.

## API Key Security

The OpenWeather API key is stored in a `.env` file instead of being written directly in the source code.

Example:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git using `.gitignore` to prevent the secret API key from being uploaded to the repository.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the Project-4 directory

```bash
cd Project-4
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment on Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create the `.env` file

Create a file named `.env` in the Project-4 directory:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own OpenWeather API key.

### 7. Run the application

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

### 8. Test using Postman

Send a GET request:

```text
http://127.0.0.1:5000/weather/Bengaluru
```

## Learning Outcomes

Through this project, I practiced:

* Third-party API integration
* Asynchronous programming
* Environment variable management
* API key security
* JSON data processing
* REST API development
* Error handling
* API testing using Postman

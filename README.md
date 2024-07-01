# Flask Hello API

## Overview

This project is a simple Flask-based web server that exposes an API endpoint. The endpoint returns a JSON response containing the client's IP address, location (city), and a personalized greeting with the current temperature.

## Features

- GET endpoint that accepts a visitor's name as a parameter
- Retrieves the client's IP address
- Uses geolocation to determine the client's city
- Fetches the current temperature for the client's location
- Returns a JSON response with all the gathered information

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository: git clone https://github.com/Nne85/flask_hello_api.git
cd flask_hello_api

2. Create a virtual environment: python -m venv venv

3.   source venv/bin/activate

4. Install the required packages:
pip install -r requirements.txt

5. Set up environment variables:
Create a `.env` file in the root directory and add the following:

GEOLOCATION_API_KEY=your_geolocation_api_key
WEATHER_API_KEY=your_weather_api_key
Replace `your_geolocation_api_key` and `your_weather_api_key` with your actual API keys.

## Configuration

The application uses different configuration classes for development, testing, and production environments. You can modify these in the `config.py` file.

## Running the Application

To run the application locally:
python run.py

The server will start on `http://0.0.0.0:5000`.

## API Usage

### Endpoint
GET /api/hello

### Query Parameters

- `visitor_name` (optional): The name of the visitor. If not provided, "Guest" will be used.

### Example Request
curl "http://localhost:5000/api/hello?visitor_name=Nnenna"

### Example Response

json response
{
  "client_ip": "127.0.0.1",
  "location": "New York",
  "greeting": "Hello, Nnenna! The temperature is 22.5 degrees Celsius in New York"
}

### Dependencies

Flask: Web framework for Python
Requests: HTTP library for making API calls
python-dotenv: For loading environment variables from a .env file

### API Keys
This project uses two external APIs:

IP Geolocation API (https://ipgeolocation.io/)
WeatherAPI (https://www.weatherapi.com/)

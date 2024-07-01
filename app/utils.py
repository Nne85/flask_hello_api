"""
This module contains functions for geolocation and weather retrieval
"""

import requests
from config import WEATHER_API_KEY, GEOLOCATION_API_KEY
import logging

logging.basicConfig(level=logging.DEBUG)

def get_geolocation(ip_address):
    """Retrieves the user's IP address from the request object."""
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={GEOLOCATION_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        logging.debug(f"Geolocation response data: {data}")
        return data.get("city", "Unknown")
    else:
        logging.error(f"Geolocation API error: {response.status_code}")
        return "Unknown"

def get_weather(city):
    """ Retrieves the user's city waether from request object"""
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        logging.debug(f"Weather response data: {data}")
        return data["current"]["temp_c"]
    else:
        logging.error(f"Weather API error: {response.status_code}")
        return "Unknown"

def get_location_and_weather(ip_address):
    city = get_geolocation(ip_address)
    temperature = get_weather(city)
    return city, temperature

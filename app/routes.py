from flask import Flask, request, jsonify
from .utils import get_location_and_weather
from . import app


@app.route('/api/hello', methods=['GET'])
def hello():
    """ The  endpoint that accepts a visitor_name parameter
    Returns:
        a json response of visitors name, city and temp
    """
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr
    city, temperature = get_location_and_weather(client_ip)

    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
    }
    return jsonify(response)

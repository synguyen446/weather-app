from flask import Flask, jsonify, request
from utils import get_location
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route("/weather")
def get_weather():

    city = request.args.get("city")
    state = request.args.get("state")

    location = get_location(city=city, state=state)

    key = "49d3b589f1ad40f8abb60800252101"
    url = "http://api.weatherapi.com/v1/forecast.json"

    query = {"key": key, "q": f"{location.latitude},{location.longitude}", "day": 5}

    response = requests.get(url=url, params=query)

    return response.json()


if __name__ == "__main__":
    app.run(debug=True)

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

    key = "08f7addab38b8791ddf8cd9d6ca5ba83"
    url = "https://api.openweathermap.org/data/2.5x/forecast"

    query = {"appid": key,
             "lat": f"{location.latitude}", 
             "lon":f"{location.longitude}"}

    response = requests.get(url=url, params=query)

    return response.json()


if __name__ == "__main__":
    app.run(debug=True)

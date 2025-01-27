from flask import Flask, jsonify, request
from utils import get_location, process_data
from flask_cors import CORS
import requests, os
from dotenv import load_dotenv


def configure():
    load_dotenv()


app = Flask(__name__)
CORS(app)


@app.route("/weather")
def get_weather():

    configure()

    city = request.args.get("city")
    state = request.args.get("state")

    location = get_location(city=city, state=state)

    if not location:
        return jsonify(message="Error location not found!")

    url = "https://api.openweathermap.org/data/3.0/onecall"

    query = {
        "appid": os.getenv("apikey"),
        "lat": f"{location.latitude}",
        "lon": f"{location.longitude}",
    }

    response = requests.get(url=url, params=query)

    return process_data(response.json(), location.address)


if __name__ == "__main__":
    app.run(debug=True)

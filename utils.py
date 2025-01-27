from geopy.geocoders import Nominatim
import json
import datetime as dt


def get_location(city, state):

    loc = Nominatim(user_agent="GetLoc")

    location = loc.geocode(f"{city}, {state}", exactly_one=True)

    return location


def _convert_to_CF(temp):
    c = int(format(temp - 273.15, ".0f"))
    f = int(format(c * 1.8 + 32, ".0f"))
    return (c, f)


def process_data(data, address):
    day = data["current"]
    icon_code = day["weather"][0]["icon"]

    data = {
        "address": address,
        "datetime": dt.datetime.fromtimestamp(day["dt"]),
        "temperature": {
            "temp": _convert_to_CF(day["temp"]),
            "feels_like": _convert_to_CF(day["feels_like"]),
            # "max": _convert_to_CF(day["main"]["temp_max"]),
            # "min": _convert_to_CF(day["main"]["temp_min"]),
        },
        "humidity": day["humidity"],
        "weather": day["weather"],
        "icon_url": f"http://openweathermap.org/img/wn/{icon_code}@2x.png",
        "visibility": day["visibility"],
        "air_pressure": day["pressure"],
        "wind_speed": day["wind_speed"],
    }

    return data

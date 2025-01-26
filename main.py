from geopy.geocoders import Nominatim
from input_validation import input_string
import requests

def get_location(city, state):

    loc = Nominatim(user_agent= "GetLoc")

    location= loc.geocode(f"{city}, {state}",exactly_one= False)

    return location

def get_weather(location):
    key = "49d3b589f1ad40f8abb60800252101"
    url = "http://api.weatherapi.com/v1/forecast.json"

    query ={
        "key": key,
        "q": f"{location.latitude},{location.longitude}",
        "day": 5
    }

    response = requests.get(url= url, params = query)

    return response.json()

def get_address(result):
    return result.address  

if __name__ == "__main__":
    city = input("Enter your city: ")
    state = input_string(prompt="Enter state abbreviation(2 characters): ",target_character=2)

    location = get_location(city,state)

    if location:
        print(list(map(get_address,location)))
    else:
        print(f"Location not found with {city}, {state}")
from geopy.geocoders import Nominatim


def get_location(city, state):

    loc = Nominatim(user_agent="GetLoc")

    location = loc.geocode(f"{city}, {state}", exactly_one=True)

    return location

def get_address(result):
    return result.address
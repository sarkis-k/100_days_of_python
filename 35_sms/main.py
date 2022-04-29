import requests
from api_key import api_key


api_url = "https://api.openweathermap.org/data/2.5/onecall"
api_param = {
    "lat": 34.052235,
    "lon": -118.243683,
    "appid": api_key
}

# response = requests.get(url="")
print(api_key)
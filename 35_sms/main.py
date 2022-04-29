import requests
from api_key import *
from twilio.rest import Client


account_sid = twilio_account_sid
auth_token = twilio_auth_token

api_url = "https://api.openweathermap.org/data/2.5/onecall"
api_param = {
    "lat": 42.824300,  # 34.052235,
    "lon": -99.750080,  # -118.243683,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url=api_url, params=api_param)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for x in range(0, 12):
    weather_condition = weather_data["hourly"][x]["weather"][0]["id"]
    if weather_condition < 700:
        will_rain = True

if will_rain:
    print("bring it")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_="+19894814919",
                     to="+18184349097"
    )
    print(message.status)





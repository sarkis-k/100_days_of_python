import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

long = response.json()["iss_position"]["longitude"]
lat = response.json()["iss_position"]["latitude"]
iss_pos = (long, lat)

print(iss_pos)

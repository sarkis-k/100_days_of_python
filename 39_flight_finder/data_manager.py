import requests
from keys import *
from flight_search import *


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_cities(self):
        response = requests.get(get_sheety_url)
        response.raise_for_status()
        data = response.json()["prices"]
        cities = []
        for x in data:
            cities.append(x["city"])

        print(cities)
        return cities

    def post_iata(self):
        response = requests.put(put_sheety_iata)
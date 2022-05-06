import requests
from keys import *


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        response = requests.get(sheety_url)
        response.raise_for_status()
        self.sheet_data = response.json()["prices"]
        return self.sheet_data

    def update_iata(self):
        for city in self.sheet_data:
            update_load = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_url}/{city['id']}",
                json=update_load
            )
            response.raise_for_status()
            print(response.text)

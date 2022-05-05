import time

import requests
from keys import *
from data_manager import DataManager
from datetime import datetime


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def iata_search(self):
        search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        today = datetime.now().strftime("%d/%m/%Y")

        cities = DataManager().get_cities()
        cities_iata = []

        iata_search_endpoint = "https://tequila-api.kiwi.com/locations/query"
        for city in cities:
            iata_param = {
                "term": city
            }
            iata_header = {
                "apikey": tequila_api
            }
            response = requests.get(url=iata_search_endpoint, params=iata_param, headers=iata_header)
            response.raise_for_status()
            data = response.json()

            cities_iata.append(data["locations"][0]["code"])

            time.sleep(2)

        return cities_iata


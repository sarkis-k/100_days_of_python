import time
import requests
from keys import *
from data_manager import DataManager
from datetime import datetime


class FlightSearch():
    # This class is responsible for talking to the Flight Search API.
    search_endpoint = "https://tequila-api.kiwi.com/v2/search"
    today = datetime.now().strftime("%d/%m/%Y")

    def iata_search(self, city):

        param = {
            "term": city
        }
        header = {
            "apikey": tequila_api
        }
        response = requests.get(url=iata_search_endpoint, params=param, headers=header)
        response.raise_for_status()
        data = response.json()
        code = data["locations"][0]["code"]
        return code



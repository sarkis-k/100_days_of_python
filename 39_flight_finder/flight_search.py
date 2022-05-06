import requests
from keys import *
from flight_data import FlightData
from datetime import datetime, timedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def iata_search(self, city):
        param = {
            "term": city
        }
        response = requests.get(url=iata_search_endpoint, params=param, headers=tequila_header)
        response.raise_for_status()
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def get_flight_values(self, destination):

        search_query = {
            "fly_from": "LAX",
            "fly_to": destination,
            "date_from": datetime.now().strftime("%d/%m/%Y"),
            "date_to": (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 15,
            "nights_in_dst_to": 21,
            "flight_type": "round",
            "curr": "USD",
            "max_stopovers": 1,
        }
        response = requests.get(
            url=tequila_endpoint,
            params=search_query,
            headers=tequila_header
        )
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flight found for {destination}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")

        return flight_data

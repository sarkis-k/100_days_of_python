from keys import *
from data_manager import *
from flight_data import *
from flight_search import *
from notification_manager import *
import requests
from pprint import pprint

data_manager = DataManager()
sheety_data = data_manager.get_data()

flight_search = FlightSearch()

if sheety_data[0]["iataCode"] == "":
    for row in sheety_data:
        row["iataCode"] = flight_search.iata_search(row["city"])
    print(f"sheet_data:\n {sheety_data}")

    data_manager.sheet_data = sheety_data
    data_manager.update_data()

for data in sheety_data:
    flight = flight_search.get_flight_values(data["iataCode"])
    time.sleep(2)

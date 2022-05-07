from flight_search import *
from data_manager import DataManager
from users import User
import time

data_manager = DataManager()
sheety_data = data_manager.get_data()

flight_search = FlightSearch()

if sheety_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheety_data]
    data_manager.city_codes = flight_search.iata_search(city_names)
    data_manager.update_iata()
    sheet_data = data_manager.get_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheety_data}


for destination_code in destinations:
    flight = flight_search.get_flight_values(destination_code)
    try:
        if destination_code["lowestPrice"] > flight.price:
            print("it's cheaper")
            message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
                print(message)
    except AttributeError:
        pass
    time.sleep(2)



user = User()
data_manager = DataManager()

if user.create_user():
    if data_manager.create_user(user):
        print("Welcome to the board")




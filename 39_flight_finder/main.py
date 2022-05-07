from flight_search import *
from data_manager import DataManager
from users import User
import time

# data_manager = DataManager()
# sheety_data = data_manager.get_data()
#
# flight_search = FlightSearch()
#
# if sheety_data[0]["iataCode"] == "":
#     for row in sheety_data:
#         row["iataCode"] = flight_search.iata_search(row["city"])
#     print(f"sheet_data:\n {sheety_data}")
#
#     data_manager.sheet_data = sheety_data
#     data_manager.update_iata()
#
# for data in sheety_data:
#     flight = flight_search.get_flight_values(data["iataCode"])
#     try:
#         if data["lowestPrice"] > flight.price:
#             print("it's cheaper")
#     except AttributeError:
#         pass
#     time.sleep(2)



user = User()

if user.create_user():
    print("Welcome to the board")


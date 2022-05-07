import requests
from keys import *
from users import User


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        response = requests.get(sheety_prices_url)
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
                url=f"{sheety_prices_url}/{city['id']}",
                json=update_load
            )
            response.raise_for_status()
            print(response.text)

    def create_user(self, user: User):
        post_user_load = {
            "user":{
                "firstname": user.name,
                "lastname": user.lastname,
                "email": user.email
            }
        }
        response = requests.post(
            url=sheety_user_url,
            json=post_user_load
        )
        response.raise_for_status()
        if response.status_code == 200:
            return True
        else:
            return False




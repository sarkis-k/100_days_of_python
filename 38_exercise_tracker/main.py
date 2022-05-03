from keys import *
import requests
from datetime import datetime

headers = {
    "x-app-id": nutrition_id,
    "x-app-key": nutrition_api,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
query = input("asa tenam: ")

post_param = {
    "query": query,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

nutrition_response = requests.post(url=nutrition_endpoint, headers=headers, json=post_param)
nutrition_json = nutrition_response.json()
print()

sheety_endpoint = "https://api.sheety.co/c4695ec5d5289ab1b3827cc2e1bd0919/pythonCoding/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in nutrition_json["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_header)

    print(sheet_response.text)
import requests

api_url = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

quiz_conn = requests.get(url=api_url, params=parameters)
quiz_conn.raise_for_status()
question_data = quiz_conn.json()["results"]


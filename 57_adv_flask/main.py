from flask import Flask, render_template
from datetime import datetime
import requests


app = Flask(__name__)

agify_api = "https://api.agify.io"
gender_api = "https://api.genderize.io"


@app.route("/")
def home():
    year = datetime.now().year
    my_name = "Sarkis"
    return render_template("index.html", year=year, name=my_name)

@app.route("/guess/<name>")
def guess(name):
    agify_param = {
        "name": name
    }
    gender_param = {
        "name": name
    }
    response = requests.get(url=agify_api, params=agify_param)
    age_num = response.json()["age"]

    response = requests.get(url=gender_api, params=gender_param)
    gender = response.json()["gender"]

    return render_template("index.html", name=name, age=age_num, gender=gender )


if __name__ == "__main__":
    app.run(debug=True)

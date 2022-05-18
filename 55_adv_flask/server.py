from flask import Flask
import random

app = Flask(__name__)
num=random.randint(0,9)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Guess the number 0-9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'

@app.route("/<int:number>")
def guessed(number):
    if number<num:
        return "<h1>too low</h1>"
    elif number>num:
        return "<h1>too high</h1>"
    else:
        return "<h1>that's right</h1>"


if __name__ == "__main__":
    app.run(debug=True)
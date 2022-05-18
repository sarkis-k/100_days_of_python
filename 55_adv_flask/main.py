from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>'


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(args):
    def wrapper():
        return f"<em>{args()}</em>"

    return wrapper


def make_underline(args):
    def wrapper():
        string = f"<u>{args()}</u>"
        return string
    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"hello sir {name} and {number}"

if __name__ == "__main__":
    app.run(debug=True)

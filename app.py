from flask import Flask, render_template, url_for


app = Flask(__name__)


USERS = {
    1063: {
      "email": "ololo@gogle.com",
      "lang": "en",
      "name": "Tubik",
      "age": "23",
    },
    2345: {
      "email": "ololo134@mail.com",
      "lang": "en",
      "name": "Slonik",
      "age": "25",
    },
    234: {
        "email": "blabla@mail.com",
        "lang": "en",
        "name": "Gnida",
        "age": "34",
    }
}

@app.route("/")
def index():
    return ("Привет")

@app.route("/users")
def users():
    return USERS


if __name__ == "__main__":
    app.run(debug=True)
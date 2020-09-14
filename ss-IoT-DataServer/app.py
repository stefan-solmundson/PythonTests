from flask import Flask, render_template
from db import Database

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('demo.html')


@app.route('/surprise')
def surprise():
    return "<h1>Blaaaaaa!</h1>"


def start_up():
    db = Database('cpu_loads.db')
    db.create()


if __name__ == "__main__":
    app.run()

# Python Internal Imports
from datetime import datetime

# External Imports
from flask import Flask, render_template, jsonify

# Application Imports
from db import Database

app = Flask(__name__)

# Initiate the Flask Application and "Database"
db = Database('cpu_loads.db')
db.create()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('demo.html')


@app.route('/surprise')
def surprise():
    return "<h1>Blaaaaaa!</h1>"


# FQDN : Fully Qualified Domain Name
#   www <-- "server", microsoft.com <-- domain
#   .com, .net, .com.au <-- TLD
# e.g. http://FQDN/api/cpu-load
@app.route('/api/cpu-load')
def api_cpu_load_default():
    history = api_cpu_load_quantity(20)
    return jsonify(history)


# e.g. http://FQDN/api/cpu-load/30
@app.route('/api/cpu-load/<quantity>')
def api_cpu_load_quantity(quantity):
    # TODO: check if integer if not set to 10
    time = datetime.now()
    data = db.get_last(quantity)
    return data


@app.errorhandler(404)
# inbuilt flask method to handle errors, takes "e" (error) as a parameter
def not_found(e):
    render_template("404.html", error=e)


if __name__ == "__main__":
    app.run()

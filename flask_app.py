
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from car_data import get_cars_by

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def index():
    return render_template("main_page.html")

@app.route('/carsearch', methods = ["GET"])
def car_search():
    print("Entering method car_search")

    year = request.args["year"] if "year" in request.args else None
    make = request.args["make"] if "make" in request.args else None
    model = request.args["model"] if "model" in request.args else None

    print("year: " + year + " make: " + make + " model: " + model)

    result = {"message": "No results"}

    result["rows"] = get_cars_by(year, make, model)


    if result["rows"]:
        result["message"] = str(len(result["rows"])) + " results"

    return jsonify(result)


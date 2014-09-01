from flask import Flask, render_template, request, redirect, url_for, json
from pprint import pformat
import model as m
import json

app = Flask(__name__)


@app.route("/")
def index():
    """
    Home page
    Chart of logged time
    Form to log time against a category
    """    
    return render_template("index.html")

@app.route("/data")
def get_data():
    """
    Return up-to-date data in json
    in> 28 days
    out> {category1: 10, category2: 15}
    """
    return
#     all_houses = m.House.objects()
#     return render_template("houses.html", houses=all_houses, nav=nav())

@app.route("/add_log", methods=['POST'])
def add_log():
    name = request.form.get("house_name")
    postcode = request.form.get("postcode")
    overview = request.form.get("overview")
    landlord_id = request.form.get("landlord_id")
    new_house = m.House()
    new_house.create(name, postcode, overview)
    new_house.save()
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)
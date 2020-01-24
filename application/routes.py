from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/')
@app.route('/home', methods = ["GET", "POST"])
def home():

    r = requests.get("https://i6swdijhm5.execute-api.eu-west-2.amazonaws.com/api")

    return render_template("index.html", title = "home", r=r.text)
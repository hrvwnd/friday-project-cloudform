from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/')
@app.route('/home', methods = ["GET", "POST"])
def home():

    r = requests.get("http://service2:5000")

    return render_template("index.html", title = "home", r=r.text)
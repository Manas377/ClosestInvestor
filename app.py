from calendar import LocaleHTMLCalendar
from webbrowser import get
from flask import Flask, render_template, request

import requests
import json
import math as math
import pandas as pd
from geopy.geocoders import Nominatim

from .utility import Utility

app = Flask(__name__)


@app.route("/")
def home():
    localhosts = ['127.0.0.1', 'localhost']
    ip_address = request.remote_addr
    if ip_address in localhosts:
        ip_address ='49.36.184.219'  # my actual ip 

    df = Utility.get_df()
    df['Coordinates'] = df['Location'].map(lambda Location: Utility.get_invester_cord(Location))
    df['Distance'] = df['Coordinates'].map(lambda Coordinates: Utility.find_dist(Coordinates, Utility.get_user_cord(ip_address)))
    df=df[df['Distance'] == df['Distance'].min()]
    
    return render_template('result.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == "__main__":
    app.run()

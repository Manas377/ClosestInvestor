import math 
import requests
import math as math
import pandas as pd
from geopy.geocoders import Nominatim

class Utility:
    @staticmethod
    def find_dist(cord1, cord2):
        R = 6373.0  
        lat1, lon1 = cord1
        lat2, lon2 = cord2

        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        dlon = lon2 - lon1   # change in coordinates

        dlat = lat2 - lat1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        distance = R * c

        # print(distance)

        return distance


    def get_user_cord(ip_address):
        try:
            response = requests.get("http://ip-api.com/json/{}".format(ip_address))
            js = response.json()
            lat = js['lat']
            long = js['lon']
            return lat, long
        except Exception as e:
            return "Unknown"

    def get_invester_cord(location):
        geolocator = Nominatim(user_agent="myApp")
        location = geolocator.geocode(location)
        return (location.latitude, location.longitude)


    def get_df(filename='Coding Assignment Investor Sample Data.csv'):
        df = pd.read_csv(filename) 
        return df


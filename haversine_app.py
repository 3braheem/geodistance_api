import math
from flask import Flask
from flask import request

app = Flask(__name__)

def haversine_distance(lat1, long1, lat2, long2):
    lat_diff = (lat2 - lat1) * math.pi / 180
    long_diff = (long2 - long1) * math.pi / 180
    lat1 = lat1 * math.pi / 180
    lat2 = lat2 * math.pi / 180

    argument = pow(math.sin(lat_diff / 2), 2) + (pow(math.sin(long_diff / 2), 2) * math.cos(lat1) * math.cos(lat2))
    double_earth_radius = 12742
    return math.asin(math.sqrt(argument)) * double_earth_radius


@app.route("/coord_dist/<lat1>/<long1>/<lat2>/<long2>")
def coordinate_distance(lat1, long1, lat2, long2):
    lat1 = float(lat1[:-1]) if lat1[-1] == "N" else float(lat1[:-1]) * -1
    lat2 = float(lat2[:-1]) if lat2[-1] == "N" else float(lat2[:-1]) * -1
    long1 = float(long1[:-1]) if long1[-1] == "E" else float(long1[:-1]) * -1
    long2= float(long2[:-1]) if long2[-1] == "E" else float(long2[:-1]) * -1

    distance = haversine_distance(lat1, long1, lat2, long2)
    return {
        "Latitude-1": lat1,
        "Longitude-1": long1,
        "Latitude-2": lat2,
        "Longitude-2": long2,
        "Distance": distance
    }

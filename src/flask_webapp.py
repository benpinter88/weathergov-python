from flask import Flask, render_template
from geopy.geocoders import Nominatim
import requests

app = Flask(__name__)

def get_location_coordinates(location_name):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def get_forecast_url(lat, lon):
    url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(url)
    data = response.json()
    return data['properties']['forecast']

def get_forecast(forecast_url):
    response = requests.get(forecast_url)
    data = response.json()
    return data['properties']['periods']

@app.route('/')
def index():
    location_name = "Boston, MA"  # or use a form to get user input
    lat, lon = get_location_coordinates(location_name)
    if lat and lon:
        forecast_url = get_forecast_url(lat, lon)
        forecast = get_forecast(forecast_url)
        return render_template('index.html', location=location_name, forecast=forecast)
    else:
        return "Location not found."

if __name__ == '__main__':
    app.run(debug=True)

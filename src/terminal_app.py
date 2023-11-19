import requests
from geopy.geocoders import Nominatim

# Get lat, lon with geopy Nominatim api client
def get_location_coordinates(location_name):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Get the forecast URL based on lat, lon
def get_forecast_url(lat, lon):
    url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(url)
    data = response.json()
    return data['properties']['forecast']

# Get the forecast data from grid URL we received in get_forecast_url
def get_forecast(forecast_url):
    response = requests.get(forecast_url)
    data = response.json()
    forecasts = data['properties']['periods']

    for forecast in forecasts:
        print(f"{forecast['name']}: {forecast['detailedForecast']}\n")

def main():
    # Replace with your location
    location_name = "Boston, MA"
    print(f"Weather forecast for: {location_name}")
    lat, lon = get_location_coordinates(location_name)
    if lat and lon:
        print(f"Coordinates for {location_name}: Latitude = {lat}, Longitude = {lon}")
        forecast_url = get_forecast_url(lat, lon)
        get_forecast(forecast_url)
        print(f"Forecast URL is: {forecast_url}")
    else:
        print("Location not found.")

if __name__ == "__main__":
    main()

import datetime as dt
import requests
from config import WEATHER_API_KEY

BASE_URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'

def get_weather_forecast(location):
    url = f'{BASE_URL}/{location}?unitGroup=metric&key={WEATHER_API_KEY}'
    response = requests.get(url)
    data = response.json()

    forecast = ""
    for day in data['days']:
        # Convert date into european format
        date = dt.datetime.strptime(day['datetime'],"%Y-%m-%d").strftime("%d.%m.%Y")
        forecast += (f"Datum: {date}, Min-Temp: {day['tempmin']}°C, Max-Temp: {day['tempmax']}°C, "
                     f"Regenwahrscheinlichkeit: {day['precip']}%, Windgeschwindigkeit: {day['windspeed']} km/h\n")
    
    return forecast


#just nessessary to test the fetch function
if __name__ == "__main__":
    location = input("Enter your location: ")
    forecast = get_weather_forecast(location)
    print(forecast)

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
        # Extract data
        min_temp = day['tempmin']
        max_temp = day['tempmax']
        precip = day['precip']
        wind_speed = day['windspeed']
        forecast += (f"Datum: {date} \n"
                     f"Min-Temp: {min_temp}°C, Max-Temp: {max_temp}°C \n"
                     f"Regenwahrscheinlichkeit: {precip}%, Windgeschwindigkeit: {wind_speed} km/h\n\n")
    
    return forecast


#just nessessary if test only the fetch function
if __name__ == "__main__":
    location = 'Berlin'
    forecast = get_weather_forecast(location)
    print(forecast)

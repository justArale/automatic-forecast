import requests
from config import BASE_URL, WEATHER_API_KEY

def get_weather_forecast(location):
    url = f'{BASE_URL}/{location}?unitGroup=metric&key={WEATHER_API_KEY}'
    response = requests.get(url)
    data = response.json()

    forecast = ""
    for day in data['days']:
        forecast += (f"Datum: {day['datetime']}, Min-Temp: {day['tempmin']}°C, Max-Temp: {day['tempmax']}°C, "
                     f"Regenwahrscheinlichkeit: {day['precip']}%, Windgeschwindigkeit: {day['windspeed']} km/h\n")
    
    return forecast


#just nessessary to test the fetch function
if __name__ == "__main__":
    location = input("Enter your location: ")
    forecast = get_weather_forecast(location)
    print(forecast)

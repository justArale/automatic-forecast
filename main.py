from weather_fetch import get_weather_forecast
from utils import save_forecast_as_html

def main():
    location = input("Enter your location: ")
    forecast = get_weather_forecast(location)
    
    # Save/Display data in 3 different ways
    save_forecast_as_html(forecast)
    print(forecast)
    # send mail

if __name__ == "__main__":
    main()

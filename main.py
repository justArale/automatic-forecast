from weather_fetch import get_weather_forecast
from utils import save_forecast_as_html
from email_sender import send_forecast_email

def main():
    location = input("Enter your location: ")
    mail_to= input ("Enter your Email: ")
    forecast = get_weather_forecast(location)
    
    # Save/Display data in 3 different ways
    save_forecast_as_html(forecast)
    print(forecast)
    send_forecast_email(forecast, location, mail_to)

if __name__ == "__main__":
    main()

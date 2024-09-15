from weather_fetch import get_weather_forecast
from utils import save_forecast_as_html
from email_sender import send_forecast_email

def main():
    # Type the location or leave empty and use Berlin by default
    location = input("Enter your location (press Enter for Berlin by default): ")
    if not location:
        location = 'Berlin'

    # Enter the recipient's email address
    mail_to= input ("Enter your Email: ")

    # Start the function to fetch the weather forecast for the specified location
    forecast = get_weather_forecast(location)
    
    # Save/Display data in 3 different ways
    save_forecast_as_html(forecast) # Save forecast in an HTML-file
    print(forecast) # Print forecast in the console
    send_forecast_email(forecast, location, mail_to) # Send forecast as an e-mail

if __name__ == "__main__":
    main()

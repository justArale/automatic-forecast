from weather_fetch import get_weather_forecast
from utils import save_forecast_as_html
from email_sender import send_forecast_email
from data_chart import create_temperatur_chart

def main():
    # Type the location or leave empty and use Berlin by default
    location = input("Enter your location (press Enter for Berlin by default): ")
    if not location:
        location = 'Berlin'

    # Enter the recipient's email address
    mail_to= input ("Enter your Email: ")

    # Start the function to fetch the weather forecast for the specified location
    forecast = get_weather_forecast(location)
    temperatur_chart = create_temperatur_chart(forecast)
    
    # Save/Display data in 3 different ways
    save_forecast_as_html(forecast, location, temperatur_chart) # Save forecast in an HTML-file
    print(f'14-Tage Wettervorhersage für {location} \n {forecast}') # Print forecast in the console
    send_forecast_email(forecast, location, mail_to, temperatur_chart) # Send forecast as an e-mail

if __name__ == "__main__":
    main()

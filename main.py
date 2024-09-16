import os
import sys

def main():
    # Import within the function to avoid unnecessary imports if config.py does not exist
    from weather_fetch import get_weather_forecast
    from utils import save_forecast_as_html
    from email_sender import send_forecast_email
    from data_chart import create_temperatur_chart

    # Type the location or leave empty and use Berlin by default
    location = input("Enter your location (press Enter for Berlin by default): ")
    if not location:
        location = 'Berlin'

    # Enter the recipient's email address or leave empty if you dont want to send an email
    mail_to= input ("Enter your Email: ")
   
    # Start the function to fetch the weather forecast for the specified location
    forecast = get_weather_forecast(location)
    temperatur_chart = create_temperatur_chart(forecast, location)
    
    # Save/Display data in 3 different ways
    save_forecast_as_html(forecast, location, temperatur_chart) # Save forecast in an HTML-file
    print(f'14-Tage Wettervorhersage für {location} \n {forecast}') # Print forecast in the console

    if mail_to and '@' in mail_to:
        send_forecast_email(forecast, location, mail_to, temperatur_chart) # Send forecast as an e-mail

if __name__ == "__main__":
# Check if running in a frozen environment
    if getattr(sys, 'frozen', False):
       # Get environment variables in frozen environment
       WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY', None)
       EMAIL_FROM = os.environ.get('EMAIL_FROM', None)
       APP_PASSWORD = os.environ.get('APP_PASSWORD', None)

       if not WEATHER_API_KEY or not EMAIL_FROM or not APP_PASSWORD:
           print("Error: Missing at least one environment variable")
           sys.exit(1) # If missing some variable, exit the function
    else: 
        # Path to the configuration file
        config_file_path = 'config.py'

        # Check if config.py exists
        if not os.path.isfile(config_file_path):
            print(f"Error: Configuration file {config_file_path} does not exist.")
            sys.exit(1) # If false, exit the function

        # If config.py is true, import and call the main function 
        import config
    main()

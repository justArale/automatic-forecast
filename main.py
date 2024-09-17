import os
import sys
from dotenv import load_dotenv

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

    # Enter the recipient's email address or leave empty if you don't want to send an email
    mail_to = input("Enter your Email (press Enter if you don't want to send an email): ")

    # Start the function to fetch the weather forecast for the specified location
    forecast = get_weather_forecast(location)
    temperatur_chart = create_temperatur_chart(forecast, location)

    # Save/Display data in 3 different ways
    save_forecast_as_html(forecast, location, temperatur_chart)  # Save forecast in an HTML file
    print(f'14 Tage Wettervorhersage für {location} \n {forecast}')  # Print forecast in the console

    if mail_to and '@' in mail_to:
        send_forecast_email(forecast, location, mail_to, temperatur_chart)  # Send forecast as an e-mail


def load_env_variables():
    # Load environment variables either from .env or directly from environment variables.
   
    # Path where the .env file should be
    exe_dir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.getcwd()
    env_file_path = os.path.join(exe_dir, '.env')

    # Load environment variables from the .env file
    if os.path.exists(env_file_path):
        load_dotenv(env_file_path)

    # Fetch the environment variables
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    EMAIL_FROM = os.getenv('EMAIL_FROM')
    APP_PASSWORD = os.getenv('APP_PASSWORD')

    return WEATHER_API_KEY, EMAIL_FROM, APP_PASSWORD


def prompt_and_save_env_variables():
    # Prompt user for missing environment variables and save them in a .env file.
    exe_dir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.getcwd()
    env_file_path = os.path.join(exe_dir, '.env')

    # Prompt for missing environment variables
    WEATHER_API_KEY = input("Enter your WEATHER_API_KEY: ")
    EMAIL_FROM = input("Enter your EMAIL_FROM (e.g., your_email@example.com): ")
    APP_PASSWORD = input("Enter your APP_PASSWORD: ")

    # Save the environment variables to a .env file
    with open(env_file_path, 'w') as env_file:
        env_file.write(f"WEATHER_API_KEY={WEATHER_API_KEY}\n")
        env_file.write(f"EMAIL_FROM={EMAIL_FROM}\n")
        env_file.write(f"APP_PASSWORD={APP_PASSWORD}\n")

    print(f"Environment variables saved in '{env_file_path}'. Please restart the application.")

if __name__ == "__main__":
# Check if running in a frozen environment
    if getattr(sys, 'frozen', False):
        # Load environment variables
        WEATHER_API_KEY, EMAIL_FROM, APP_PASSWORD = load_env_variables()

        # If any of the environment variables are missing, prompt the user to enter them and save them
        if not WEATHER_API_KEY or not EMAIL_FROM or not APP_PASSWORD:
            print("Environment variables are missing. Please enter the following:")
            prompt_and_save_env_variables()
            sys.exit(1)  # Exit after saving environment variables for restart
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
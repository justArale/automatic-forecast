# Helper function to save the weather data in forecast.html
def save_forecast_as_html(forecast, location):
    with open('forecast.html', 'w') as file:
        file.write(f'14-Tage Wettervorhersage für {location} \n {forecast}')

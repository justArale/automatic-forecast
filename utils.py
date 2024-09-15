# Helper function to save the weather data in forecast.html
def save_forecast_as_html(forecast):
    with open('forecast.html', 'w') as file:
        file.write(forecast)

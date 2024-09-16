# Helper function to save the weather data in forecast.html
def save_forecast_as_html(forecast, location, temperatur_chart):
    with open('index.html', 'w') as file:
        file.write(f'''
        <html lang="en">
        <head>
                   <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>14-Day Weather Forecast</title>
        </head>
        <body>
            <h1>14-Day Weather Forecast for {location}</h1>
            <pre>{forecast}</pre>
            <h2>Temperature Chart</h2>
            <img src="{temperatur_chart}" alt="Temperature Chart">
        </body>
        </html>
        ''')

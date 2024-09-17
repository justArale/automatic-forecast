import os
import sys

# Helper function to save the weather data in forecast.html
def save_forecast_as_html(forecast, location, temperatur_chart):
    # Determine the directory where the executable is located
    if getattr(sys, 'frozen', False):
        # If running in a frozen environment (e.g., PyInstaller)
        html_file_path = 'forecast.html'
        # Directory where the .exe is located
        exe_dir = os.path.dirname(sys.executable)
    else:
        # If running in a normal Python environment
        html_file_path = 'index.html'
        exe_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the path for the HTML file in the same directory as the executable
    html_file_path = os.path.join(exe_dir, html_file_path)

    # Write the HTML content to the file
    with open(html_file_path, 'w') as file:
        file.write(f'''
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>14 Tage Wettervorhersage</title>
        </head>
        <body>
            <h1>14 Tage Wettervorhersage für {location}</h1>
            <pre>{forecast}</pre>
            <h2>Temperatur Chart</h2>
            <img src="{temperatur_chart}" alt="Temperature Chart">
        </body>
        </html>
        ''')

    print(f"Forecast has been saved to {html_file_path}")

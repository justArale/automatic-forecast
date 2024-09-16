import matplotlib.pyplot as plt
import numpy as np

def create_temperatur_chart(forecast):
    # Get data from forecast
    days = []
    min_temps = []
    max_temps = []
    
    for line in forecast.splitlines():
        if 'Datum' in line:
            # Split line to date, temp-min and temp-max
            parts = line.split(', ')
            date = parts[0].split(': ')[1]
            min_temp = float(parts[1].split(': ')[1][:-2])  # Remove °C
            max_temp = float(parts[2].split(': ')[1][:-2])
            
            days.append(date)
            min_temps.append(min_temp)
            max_temps.append(max_temp)
    
    # Start chart
    plt.figure(figsize=(8, 12)) # Size of the chart: width=10 zoll and height=6 zoll
    plt.plot(days, min_temps, label='Min Temperature', color='blue', marker='o')
    plt.plot(days, max_temps, label='Max Temperature', color='red', marker='o')
    
    plt.fill_between(days, min_temps, max_temps, color='gray', alpha=0.1)
    
    plt.title('14-Day Temperature Forecast')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=90) # Set the date vertical 
    plt.legend()
    
    # Save chart as image
    chart_filename = 'temperature_chart.png'
    plt.savefig(chart_filename)
    plt.close()  # Close chart
    
    return chart_filename

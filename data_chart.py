import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def create_temperatur_chart(forecast, location):
    # Get data from forecast
    days = []
    min_temps = []
    max_temps = []

    lines = forecast.strip().split('\n')
    
    i = 0
    while i < len(lines):
        if 'Datum' in lines[i]:
            try:
                # Extract date
                date = lines[i].split(': ')[1].strip()
                
                # Extract temperature data
                min_temp_str = lines[i+1].split(', ')[0].split(': ')[1][:-3].strip()  # Remove °C
                max_temp_str = lines[i+1].split(', ')[1].split(': ')[1][:-3].strip()  # Remove °C

                min_temp = float(min_temp_str)
                max_temp = float(max_temp_str)
                
                days.append(date)
                min_temps.append(min_temp)
                max_temps.append(max_temp)
                
                # Debugging output
                # print(f"Processed date: {date}, Min Temp: {min_temp}, Max Temp: {max_temp}")
                
                # Move to the next block of data
                i += 4
            except (IndexError, ValueError) as e:
                print(f"Error parsing line: {lines[i]}. Error: {e}")
                i += 1  # Move to the next line in case of an error
        else:
            i += 1

    if not days:
        raise ValueError("No valid data found to create the chart.")

    # Convert dates to a format that matplotlib can handle
    x = np.arange(len(days))
    
    # Start chart
    plt.figure(figsize=(12, 8))  # Size of the chart: width=12 inches and height=8 inches
    plt.plot(x, min_temps, label='Min Temperatur', color='blue', marker='o')
    plt.plot(x, max_temps, label='Max Temperatur', color='red', marker='o')
    
    plt.fill_between(x, min_temps, max_temps, color='gray', alpha=0.2)
    
    plt.title(f'Übersicht der Temperaturen in {location} für die nächsten 14 Tage')
    plt.xlabel('Datum')
    plt.ylabel('Temperatur (°C)')
    # x: Convert every day, days: Display the date instead of the day-indexnumber, rotation: Set the date vertical
    plt.xticks(x, days, rotation=90)  
    plt.legend()
    
    # Save chart as image
    chart_filename = 'temperature_chart.png'
    plt.tight_layout()  # Adjust layout to avoid clipping
     # Determine the directory where the executable is located
    if getattr(sys, 'frozen', False):
        # If running in a frozen environment (e.g., PyInstaller)
        # Directory where the .exe is located
        exe_dir = os.path.dirname(sys.executable)
        chart_path = os.path.join(exe_dir, chart_filename)
    else:
        # If running in a normal Python environment
        chart_path = chart_filename
    plt.savefig(chart_path)

    plt.close()  # Close chart
    
    return chart_filename

# Weather Forecast Application

## Overview

This Python application fetches a 14-day weather forecast for a specified location using the Visual Crossing Weather API. The forecast includes minimum and maximum temperatures, precipitation probability, and wind speed. The application can display the forecast in the console, save it as an HTML file, and send it via email.

## Features

- Fetches 14-day weather forecast data
- Displays forecast in the console
- Saves forecast data as an HTML file
- Sends forecast data via email

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/justArale/automatic-forecast.git
   cd automatic-forecast
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # for Mac
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your environment:**

   Create a `config.py` file in the project directory with the following content:

   ```env
   WEATHER_API_KEY=your_api_key_here
   EMAIL_ADDRESS=your_email@gmail.com
   APP_PASSWORD=your_app_password
   ```

   Replace `your_api_key_here` with your Visual Crossing Weather API key, and `your_email@gmail.com` and `your_app_password` with your Gmail address and app password.

## Usage

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Input the location and email address when prompted.**

   - **Location:** Enter the location for which you want to fetch the weather forecast. Press Enter to use Berlin as the default location.
   - **Email:** Enter the recipient's email address where you want to send the weather forecast.

## Code Structure

- `main.py`: The main script to run the application.
- `weather_fetch.py`: Contains the function to fetch weather forecast data from the API.
- `utils.py`: Contains utility functions, to save the forecast data as an HTML file.
- `email_sender.py`: Contains the function to send the forecast data via email.
- `data_chart.py` Contains functionality to generate and save a chart image displaying the minimum and maximum temperatures over a specified period.
- `config.py`: File to store sensitive information (not included in the repository for security reasons).

## Acknowledgements

- [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api) for weather data.
- [Gmail SMTP](https://support.google.com/a/answer/176600) for sending emails.
- [App-Password](https://support.google.com/mail/answer/185833?hl=en) documentation of Gmail.

## Troubleshooting

- **Connection Error**: If you encounter issues with fetching weather data, ensure that your API key is valid and that you have a working internet connection.
- **Email Error**: If you face issues sending emails, check that your Gmail app password is correctly set up and that less secure app access is enabled.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/justArale/automatic-forecast/blob/main/LICENSE) file for details.

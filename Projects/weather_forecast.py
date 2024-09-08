# weather_forecast.py

import requests

# Constants
API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    """Fetch the weather forecast for a city."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    """Display weather information."""
    if data:
        city = data.get('name')
        weather = data.get('weather')[0].get('description')
        temp = data.get('main').get('temp')
        print(f"Weather in {city}: {weather.capitalize()}")
        print(f"Temperature: {temp}°C")
    else:
        print("Unable to retrieve weather data. Please check the city name or try again later.")

def main():
    print("Weather Forecast Application")
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()

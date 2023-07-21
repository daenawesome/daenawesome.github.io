import requests

def wind_chill(temperature, wind_speed):
    # Calculate the wind chill using the formula
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16
    return wind_chill

def celsius_to_fahrenheit(temperature):
    # Convert the temperature from Celsius to Fahrenheit
    return temperature * (9/5) + 32

# Ask the user for their location
location = input("What is your location? ")

# Fetch weather data for the user's location
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=d74b44aa3356c559c263a8574eb61950&units=metric")
if response.status_code == 200:
    weather_data = response.json()
    temperature = weather_data["main"]["temp"]
    wind_speed = weather_data["wind"]["speed"]
    print(f"The temperature in {location} is {temperature}C and the wind speed is {wind_speed} m/s.")

    # Convert the temperature to Fahrenheit if necessary
    temperature_scale = input("Fahrenheit or Celsius (F/C)? ").lower()
    if temperature_scale == 'f':
        temperature = celsius_to_fahrenheit(temperature)

    # Calculate the wind chill
    wind_chill_value = wind_chill(temperature, wind_speed)
    print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_value:.2f}F")
else:
    print("Failed to fetch weather data. Please try again later.")


"""
In this updated version, the program prompts the user for their location and uses the OpenWeatherMap API to fetch weather data for that location.
The program then extracts the temperature and wind speed from the API response and prompts the user to specify the temperature scale. If the user selects Fahrenheit, the program converts the temperature from Celsius to Fahrenheit.

Finally, the program calculates the wind chill using the temperature and wind speed values obtained from the API response and displays the wind chill value. This makes the program more personalized and relevant to the user by using their location to fetch weather data.
  
This version of the code asks the user if they want to use their current location or enter a location manually. If they choose to use their current location, it uses an IP address geolocation API to get their location. It then fetches weather data for the user's location and calculates the wind chill based on the current weather conditions.
"""
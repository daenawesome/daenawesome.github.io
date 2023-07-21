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

    # Recommend suitable clothing based on the wind chill and temperature
    if wind_chill_value < 0:
        print("It's very cold! Wear a heavy coat, gloves, and a hat to stay warm.")
    elif wind_chill_value < 10:
        print("It's chilly! Wear a jacket or sweater to stay warm.")
    else:
        print("It's comfortable outside! Wear whatever you like.")
else:
    print("Failed to fetch weather data. Please try again later.")

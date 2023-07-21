import requests

def wind_chill(temperature, wind_speed):
    # Calculate the wind chill using the formula
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16

    # Determine the wind chill level based on the wind chill value
    if wind_chill < 0:
        message = "It's very cold! Wear a heavy coat, gloves, and a hat to stay warm."
    elif wind_chill < 10:
        message = "It's chilly! Wear a jacket or sweater to stay warm."
    else:
        message = "It's comfortable outside! Wear whatever you like."

    return wind_chill, message


def celsius_to_fahrenheit(temperature):
    # Convert the temperature from Celsius to Fahrenheit
    return temperature * (9/5) + 32

def get_user_location():
    # Use an IP address geolocation API to get the user's location
    response = requests.get("https://ipapi.co/json")
    if response.status_code == 200:
        location_data = response.json()
        city = location_data["city"]
        state = location_data["region"]
        country = location_data["country_name"]
        return f"{city}, {state}, {country}"
    else:
        return None

# Ask the user if they want to use their current location or enter a location manually
location_choice = input("Would you like to use your current location (C) or enter a location manually (M)? ").lower()

if location_choice == 'c':
    # Get the user's location automatically using their IP address
    location = get_user_location()
    if location is None:
        print("Failed to get your location. Please try again later or enter a location manually.")
        location_choice = 'm'
    else:
        print(f"Your location is: {location}")
else:
    # Ask the user for their location
    location = input("Please enter a location: ")

# Fetch weather data for the user's location
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=d74b44aa3356c559c263a8574eb61950&units=metric")
if response.status_code == 200:
    # Weather data was successfully retrieved
    weather_data = response.json()
    temperature = weather_data["main"]["temp"]
    wind_speed = weather_data["wind"]["speed"]
    print(f"The temperature in {location} is {temperature}C and the wind speed is {wind_speed} m/s.")

    # Convert the temperature to Fahrenheit if necessary
    temperature_scale = input("Fahrenheit or Celsius (F/C)? ").lower()
    if temperature_scale == 'f':
        temperature = celsius_to_fahrenheit(temperature)

    # Calculate the wind chill
    wind_chill_value, wind_chill_message = wind_chill(temperature, wind_speed)
    print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_value:.2f}F")
    print(wind_chill_message)
else:
    # Weather data was not successfully retrieved
    if response.status_code == 404:
        print(f"Could not find weather data for {location}. Please check your spelling and try again.")
    else:
        print("Failed to fetch weather data. Please try again later.")

"""
This updated new version features functions to convert Celsius to Fahrenheit and to calculate the wind chill based on the input values. 
It also uses the Requests library to make HTTP requests using my personal key to the OpenWeatherMap API and an IP geolocation API to get the user's location.

The program prompts the user to choose between using their current location or entering a location manually, 
and provides appropriate messages depending on the success or failure of fetching the weather data.

The program then converts the temperature from Celsius to Fahrenheit if the user requests it, 
and calculates the wind chill value using a formula based on the temperature and wind speed. 
It also provides a message to the user based on the wind chill value, to suggest appropriate clothing to wear for the weather conditions.
"""
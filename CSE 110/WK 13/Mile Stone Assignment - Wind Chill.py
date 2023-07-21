def wind_chill(temperature, wind_speed):
    # Calculate the wind chill using the formula
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16
    return wind_chill

def celsius_to_fahrenheit(temperature):
    # Convert the temperature from Celsius to Fahrenheit
    return temperature * (9/5) + 32

# Ask the user for the temperature and temperature scale (Celsius or Fahrenheit)
temperature = float(input("What is the temperature? "))
temperature_scale = input("Fahrenheit or Celsius (F/C)? ")

# Convert the temperature to Fahrenheit if necessary
if temperature_scale.lower() == 'c':
    temperature = celsius_to_fahrenheit(temperature)

# Loop through the wind speeds and calculate the wind chill for each one
for wind_speed in range(5, 61, 5):
    wind_chill_value = wind_chill(temperature, wind_speed)
    print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_value:.2f}F")

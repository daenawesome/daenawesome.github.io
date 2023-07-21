ANSI_YELLOW = "\u001b[33m"
ANSI_RESET = "\u001b[0m"

while True:
    def fahrenheit_to_celsius(fahrenheit):
      celsius = (fahrenheit - 32) * 5/9
      return celsius

    fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equivalent to {celsius:.1f}°C.")

    run_again = input(ANSI_YELLOW + "\nWould you like to run the script again? (y/n)\n" + ANSI_RESET)
    if run_again == "n":
        print("BYE!")
        break
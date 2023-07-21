import math

def calc_velocity(m, g, t, p, A, C):
    # Calculate c
    c = (1/2) * p * A * C

    # Calculate the overall velocity
    v = math.sqrt((m*g)/c) * (1 - math.exp(-c*t/m))

    return v

def main():
    try:
        # Prompt the user for the mass of the object
        m = float(input("Enter the mass of the object (in kg): "))

        # Prompt the user for the acceleration due to gravity
        g = float(input("Enter the acceleration due to gravity (in m/s^2): "))

        # Prompt the user for the time
        t = float(input("Enter the time (in seconds): "))

        # Prompt the user for the density of the fluid
        p = float(input("Enter the density of the fluid (in kg/m^3): "))

        # Prompt the user for the cross sectional area of the object
        A = float(input("Enter the cross sectional area of the object (in m^2): "))

        # Prompt the user for the drag constant
        C = float(input("Enter the drag constant: "))

        # Calculate and display the overall velocity
        v = calc_velocity(m, g, t, p, A, C)
        print("Overall velocity = {:.3f} m/s".format(v))

        # Convert the velocity from m/s to km/h
        v_kmh = v * 3.6
        print("Overall velocity = {:.3f} km/h".format(v_kmh))
    except ValueError:
        print("Invalid input. Please enter a positive number.")

if __name__ == "__main__":
    main()

"""
includes a function calc_velocity that calculates the velocity based on the given input values. 
The main function prompts the user for the required input values, calculates and displays the overall velocity, 
and converts the velocity from m/s to km/h.
"""
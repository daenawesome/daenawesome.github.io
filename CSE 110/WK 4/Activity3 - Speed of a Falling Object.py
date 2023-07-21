import math

def calc_velocity(m, g, t, p, A, C):
    c = (1/2) * p * A * C
    v = math.sqrt((m*g)/c) * (1 - math.exp(-c*t/m))
    return v

def main():
    try:
        print("Select the unit of measurement for mass:")
        print("1. Kilograms")
        print("2. Pounds")
        mass_unit = int(input("Enter the number of the selected unit: "))
        if mass_unit == 1:
            m = float(input("Enter the mass of the object (in kg): "))
        elif mass_unit == 2:
            m = float(input("Enter the mass of the object (in pounds): "))
            m = m * 0.453592
        else:
            raise ValueError

        print("Select the unit of measurement for gravity:")
        print("1. Meters per second squared")
        print("2. Feet per second squared")
        gravity_unit = int(input("Enter the number of the selected unit: "))
        if gravity_unit == 1:
            g = float(input("Enter the acceleration due to gravity (in m/s^2): "))
        elif gravity_unit == 2:
            g = float(input("Enter the acceleration due to gravity (in ft/s^2): "))
            g = g * 0.3048
        else:
            raise ValueError

        t = float(input("Enter the time (in seconds): "))
        p = float(input("Enter the density of the fluid (in kg/m^3): "))
        print("Select the shape of the object:")
        print("1. Sphere")
        print("2. Cylinder")
        shape = int(input("Enter the number of the selected shape: "))

        if shape == 1:
            A = float(input("Enter the radius of the sphere (in m): "))
            A = math.pi * A**2
            C = 0.5
        elif shape == 2:
            A = float(input("Enter the radius of the cylinder (in m): "))
            A = math.pi * A**2
            C = 1.1
        else:
            raise ValueError

        v = calc_velocity(m, g, t, p, A, C)
        print("Overall velocity = {:.3f} m/s".format(v))
        v_kmh = v * 3.6
        print("Overall velocity = {:.3f} km/h".format(v_kmh))
    except ValueError:
        print("Invalid input. Please enter a valid shape number.")

if __name__ == "__main__":
    main()

"""
calculates the velocity of an object based on its mass, acceleration due to 
gravity, time, density of the fluid, cross sectional area, and drag constant. 
The user can select the units of measurement for mass and gravity, as well as the shape of the object.
"""
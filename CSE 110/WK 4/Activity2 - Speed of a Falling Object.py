import math

def calc_velocity(m, g, t, p, A, C):
    c = (1/2) * p * A * C
    v = math.sqrt((m*g)/c) * (1 - math.exp(-c*t/m))
    return v

def main():
    try:
        m = float(input("Enter the mass of the object (in kg): "))
        g = float(input("Enter the acceleration due to gravity (in m/s^2): "))
        t = float(input("Enter the time (in seconds): "))
        p = float(input("Enter the density of the fluid (in kg/m^3): "))
        print("Select the shape of the object:")
        print("1. Sphere")
        print("2. Cylinder")
        shape = int(input("Enter the number of the selected shape: "))

        if shape == 1:
            # Sphere
            A = float(input("Enter the radius of the sphere (in m): "))
            A = math.pi * A**2
            C = 0.5
        elif shape == 2:
            # Cylinder
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
    Includes a function 'calc_velocity' that calculates the velocity based on the given input values. 
    The main function prompts the user for the required input values, including the shape of the object. 
    Based on the selected shape, the program calculates the cross sectional area and drag constant. 
    It then calculates and displays the overall velocity, and converts the velocity from m/s to km/h
    """
import math

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

# Calculate c
c = (1/2) * p * A * C

# Display c to three decimal places
print("c = {:.3f}".format(c))

# Calculate the overall velocity
v = math.sqrt((m*g)/c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

# Display the overall velocity to three decimal places
print("Overall velocity = {:.3f} m/s".format(v))

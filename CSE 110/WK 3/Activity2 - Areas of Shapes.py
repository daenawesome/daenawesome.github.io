import math

# Prompt user for single length value in centimeters
length = float(input("Enter a length value in centimeters: "))

# Convert length value to meters
length_in_meters = length / 100

# Compute area of square in square centimeters and square meters
square_area_sq_cm = length ** 2
square_area_sq_m = square_area_sq_cm / 10000

# Compute area of circle in square centimeters and square meters
circle_radius = length / 2
circle_area_sq_cm = math.pi * circle_radius ** 2
circle_area_sq_m = circle_area_sq_cm / 10000

# Compute volume of cube in cubic centimeters and cubic meters
cube_volume_cu_cm = length ** 3
cube_volume_cu_m = cube_volume_cu_cm / 1000000

# Compute volume of sphere in cubic centimeters and cubic meters
sphere_radius = length / 2
sphere_volume_cu_cm = (4/3) * math.pi * sphere_radius ** 3
sphere_volume_cu_m = sphere_volume_cu_cm / 1000000

# Print results
print(f"The area of the square is: {square_area_sq_cm:.2f} square centimeters or {square_area_sq_m:.6f} square meters")
print(f"The area of the circle is: {circle_area_sq_cm:.2f} square centimeters or {circle_area_sq_m:.6f} square meters")
print(f"The volume of the cube is: {cube_volume_cu_cm:.2f} cubic centimeters or {cube_volume_cu_m:.6f} cubic meters")
print(f"The volume of the sphere is: {sphere_volume_cu_cm:.2f} cubic centimeters or {sphere_volume_cu_m:.6f} cubic meters")

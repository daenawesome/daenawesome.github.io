import math

# prompt for the length of a side of the square
length = float(input("What is the length of a side of the square (in cm)? "))

# calculate the area of the square
square_area = length ** 2

# display the area of the square in square centimeters and square meters
print(f"The area of the square is: {square_area:.2f} sq cm")
#print(f"The area of the square is: {square_area * 1e-4:.2f} sq m")

# prompt for the length and width of the rectangle
length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))

# calculate the area of the rectangle
rectangle_area = length * width

# display the area of the rectangle in square centimeters and square meters
print(f"The area of the rectangle is: {rectangle_area:.2f} sq cm")
#print(f"The area of the rectangle is: {rectangle_area * 1e-4:.2f} sq m")

# prompt for the radius of the circle
radius = float(input("What is the radius of the circle (in cm)? "))

# calculate the area of the circle
circle_area = math.pi * radius ** 2

# display the area of the circle in square centimeters and square meters
print(f"The area of the circle is: {circle_area:.2f} sq cm")
#print(f"The area of the circle is: {circle_area * 1e-4:.2f} sq m")

# calculate the volume of the cube
cube_volume = length ** 3

# display the volume of the cube in cubic centimeters and cubic meters
print(f"The volume of the cube is: {cube_volume:.2f} cu cm")
#print(f"The volume of the cube is: {cube_volume * 1e-6:.2f} cu m")

# calculate the volume of the sphere
sphere_volume = (4/3) * math.pi * radius ** 3

# display the volume of the sphere in cubic centimeters and cubic meters
print(f"The volume of the sphere is: {sphere_volume:.2f} cu cm")
#print(f"The volume of the sphere is: {sphere_volume * 1e-6:.2f} cu m")

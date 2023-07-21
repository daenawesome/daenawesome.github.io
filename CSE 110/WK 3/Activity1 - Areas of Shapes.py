import math

# function to calculate area of square
def area_square(side):
    return side**2

# function to calculate area of rectangle
def area_rectangle(length, width):
    return length * width

# function to calculate area of circle
def area_circle(radius):
    return math.pi * radius**2

# function to calculate volume of cube
def volume_cube(side):
    return side**3

# function to calculate volume of sphere
def volume_sphere(radius):
    return (4/3) * math.pi * radius**3

# read length from user
length = float(input("Enter the length in centimeters: "))

# calculate and print areas of square, circle and volumes of cube, sphere
print("Area of square: %.2f square centimeters, %.2f square meters" % (area_square(length), area_square(length/100)))
print("Area of circle: %.2f square centimeters, %.2f square meters" % (area_circle(length), area_circle(length/100)))
print("Volume of cube: %.2f cubic centimeters, %.2f cubic meters" % (volume_cube(length), volume_cube(length/100)))
print("Volume of sphere: %.2f cubic centimeters, %.2f cubic meters" % (volume_sphere(length), volume_sphere(length/100)))
import math

def compute_area_square(side):
    return side ** 2

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * (radius ** 2)

while True:
    shape = input("What shape do you have? (square, rectangle, circle) ")
    if shape == "square":
        side = float(input("What is the length of a side? "))
        area = compute_area_square(side)
        print("The area of the square is:", area)
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area_rectangle(length, width)
        print("The area of the rectangle is:", area)
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area_circle(radius)
        print("The area of the circle is:", area)
    elif shape == "quit":
        break
    else:
        print("Invalid shape. Please try again.")

"""
This program uses three functions to compute the areas of squares, rectangles, and circles. 
The compute_area_square function takes a single parameter side and returns the area of the square. 
The compute_area_rectangle function takes two parameters length and width and returns the area of the rectangle. 
The compute_area_circle function takes a single parameter radius and returns the area of the circle using the math.pi 
constant and the formula pi * r^2.

The program then uses a while loop to repeatedly prompt the user for the shape of the object, 
and then the length(s) or radius, and then calls the appropriate function to compute the area. 
If the user enters "quit", the loop is exited. Otherwise, if an invalid shape is entered, the 
program prints an error message and prompts the user again. The computed area is then displayed 
using the print function.
"""
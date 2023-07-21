import math

# variable = input('What is the length of a side of the square? ')
# sq_area = float(variable)**2
# print(f'The area of the square is : {sq_area}')
# length = input('What is the length of rectangle? ')
# width = input('What is the width of the rectangle? ')
# rec_area = float(length) * float(width)
# print(f'The area of the rectangle is: {rec_area}')
# variable = input('What is the radius of the circle? ')
# circ_area = math.pi * float(variable)**2
# print(f'The area of the circle is: {circ_area}')

# ------------------------- stretch ----------------------
length = float(input('Type the length value: '))
sq_area = length**2
circ_area = math.pi * length**2
cube_vol = length**3
sphere_vol = (4/3) * math.pi * length**3

print(f'The area of the square is: {sq_area}\n\
The area of the circle is: {circ_area}\n\
The volume of the cube is: {cube_vol}\n\
The volume of the sphere is: {sphere_vol}\n')
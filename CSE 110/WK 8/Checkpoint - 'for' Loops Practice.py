# Program to display items in a list and numbers from a range

# Step 1: Declare a list of colors
colors = ["red", "blue", "green", "yellow"]

# Step 2: Use a for loop to iterate through the list and display each item
for color in colors:
    print(color)

# Step 3: Use a for loop to display the numbers 1-8
for i in range(1,9):
    print(i)

# Step 4: Use a for loop to display the even numbers 2-20
for i in range(2,21,2):
    print(i)


"""
range(start, stop, step) is used to iterate through numbers 
in steps, where start is the starting number, stop is the ending 
number, and step is the difference between each number in the sequence.
"""